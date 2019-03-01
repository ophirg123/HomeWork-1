sum = 3.0
x = 2.0
for i in range(1000):
    if i % 2 == 0:
        sum = sum + (4 / (x * (x + 1) * (x + 2)))
    else:
        sum = sum - (4 / (x * (x + 1) * (x + 2)))
    x = x + 2

print(float(sum))


try:
    value=int(input("Type a number:"))
except ValueError:
    print("This is not a whole number.")