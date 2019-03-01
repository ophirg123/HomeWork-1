sum = 3.0
x = 2.0
for i in range(1000):
    if i % 2 == 0:
        sum = sum + (4 / (x * (x + 1) * (x + 2)))
    else:
        sum = sum - (4 / (x * (x + 1) * (x + 2)))
    x = x + 2

def make_pi():
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(30):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10*q, 10*(r-m*t), t, k, (10*(3*q+r))//t - 10*m, x
        else:
            q, r, t, k, m, x = q*k, (2*q+r)*x, t*x, k+1, (q*(7*k+2)+r*x)//(t*x), x+2


#my_array = []

#for i in make_pi():
#    my_array.append(str(i))

#my_array = my_array[:1] + ['.'] + my_array[1:]
#big_string = "".join(my_array)
#rint("here is a big string:\n %s" % big_string)
#print(len(big_string))

import subprocess


file = '302363049.py'
state = subprocess.call(["python", file, "--task", "fibonacci", "--N", '153'])
#print(state)