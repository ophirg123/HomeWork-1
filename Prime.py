List_length = 0
prime_List = [1]
optional_List = list(range(10000))
for each_number in range(2, 10000):
    if optional_List[each_number]:
        prime_List.append(each_number)
        for every_multiple_of_the_prime in range(each_number * 2, 10000, each_number):
            optional_List[every_multiple_of_the_prime] = 0
    List_length = len(prime_List)
    if List_length == 1000:
        break
print(prime_List)
print(List_length)