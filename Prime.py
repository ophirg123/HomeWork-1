n0 = 0
n1 = 1
count = 1
while count < 153:
       nth = n0 + n1
       # update values
       n0 = n1
       n1 = nth
       count += 1
print(nth)