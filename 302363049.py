import argparse

parser = argparse.ArgumentParser(description='Pi number for N digits, Nth prime number, Nth Fibonacci number')  # Parse Command-line argument
parser.add_argument('--task', type=str, required=True, help='Type pi / prime / Fibonacci')
parser.add_argument('--N', type=int, required=True, help='Integer Number Between 1 and 1000')
args = parser.parse_args()


TaskList = ['pi','prime','fibonacci']  # List of optional tasks
if args.task in TaskList and args.N in range(1, 1001):
    if args.task == 'pi':
        print('pi')
    elif args.task == 'prime':
        List_length = 0
        prime_List = [1]
        optional_List = list(range(10000))
        for each_number in range(2, 10000):
            if optional_List[each_number]:
                prime_List.append(each_number)
                for every_multiple_of_the_prime in range(each_number * 2, 10000, each_number):
                    optional_List[every_multiple_of_the_prime] = 0
            List_length = len(prime_List)
            if List_length == 1001:
                break
        print(prime_List[args.N])
    else:
        f0 = 0
        f1 = 1
        while args.N > 0:
            a = a
        print('fibonacci')
else:
    print('Wrong input')
    exit()