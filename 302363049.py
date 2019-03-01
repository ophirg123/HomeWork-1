import argparse
#import time
#start = time.time()

parser = argparse.ArgumentParser(description='Pi number for N digits, Nth prime number, Nth Fibonacci number')
# Parse Command-line argument, take arguments from the CMD and parse to the .py variables.
parser.add_argument('--task', type=str, required=True, default='', help='Type pi / prime / Fibonacci')
parser.add_argument('--N', type=str, required=True, default='', help='Integer Number Between 1 and 1000')
args = parser.parse_args()

TaskList = ['pi', 'prime', 'fibonacci']  # List of optional tasks

try:
    value = int(args.N)
    # Int input validation
except ValueError:
    print('Wrong input')
    exit()

Requested_number = int(float(args.N))
if args.task in TaskList and Requested_number in range(1, 1001):
    if args.task == 'pi':
        def make_pi():
            q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
            for j in range(5000):
                if 4 * q + r - t < m * t:
                    yield m
                    q, r, t, k, m, x = 10 * q, 10 * (r - m * t), t, k, (10 * (3 * q + r)) // t - 10 * m, x
                else:
                    q, r, t, k, m, x = q * k, (2 * q + r) * x, t * x, k + 1, (q * (7 * k + 2) + r * x) // (t * x), x + 2


        my_array = []
        for i in make_pi():
            my_array.append(str(i))

        my_array = my_array[:1] + ['.'] + my_array[1:]
        big_string = "".join(my_array)
        requested_pi = (big_string[0:Requested_number+2])
        requested_pi = str(requested_pi)
        length_requested_pi = len(requested_pi)
        for Slice in range(0, length_requested_pi, 40):
            #  Slice the the output number to 40 digits each line
            print(requested_pi[Slice:Slice + 40])

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
            if List_length == 1001:  # Make sure that all input numbers will receive output from the prime list.
                break
        print(prime_List[Requested_number])
    else:
        n0 = 0
        n1 = 1
        count = 1
        if Requested_number == 1:
            print(1)
        else:
            while count < Requested_number:
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
#end = time.time()
#print(end - start)