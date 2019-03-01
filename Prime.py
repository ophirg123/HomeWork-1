PrimeList = []
num = 0
while len(PrimeList) < 1000:
    for num in range(1,2000):
        for i in range(2, 2000):
            if num % i == 0:
                PrimeList.append(num)
            break
        print(PrimeList)
