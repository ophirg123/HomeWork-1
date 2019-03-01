import argparse
import time
start = time.time()

parser = argparse.ArgumentParser(description='Pi number for N digits, Nth prime number, Nth Fibonacci number')
# Parse Command-line argument, take arguments from the CMD and parse to the .py variables.
parser.add_argument('--task', type=str, required=True, help='Type pi / prime / Fibonacci')
parser.add_argument('--N', type=int, required=True, help='Integer Number Between 1 and 1000')
args = parser.parse_args()

TaskList = ['pi', 'prime', 'fibonacci']  # List of optional tasks
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
                    # Change every multiplication of the prime number in the option_list to 0 and then the list,
                    # for example, if 2 is the prime number, every 2*X in the range of the optional list will be 0.
                    optional_List[every_multiple_of_the_prime] = 0
            List_length = len(prime_List)
            if List_length == 1001:  # Make sure that all input numbers will be receive output from the prime list.
                break
        print(prime_List[args.N])
    else:
        n0 = 0
        n1 = 1
        count = 1
        if args.N == 1:
            print(1)
        else:
            while count < args.N:
                nth = n0 + n1
                # update values as the fibonacci equation
                n0 = n1
                n1 = nth
                count += 1
            fibonacci_number = str(nth)
            length_fibonacci_number = len(fibonacci_number)
            for Slice in range(0, length_fibonacci_number, 40):
                #  Slice the the output number to 40 digits each line
                print(fibonacci_number[Slice:Slice+40])
else:
    print('Wrong input')
    exit()
end = time.time()
print(end - start)