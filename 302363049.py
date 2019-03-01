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
        PrimeList = []
        num = 0
        for num in range(1,2000):
            while len(PrimeList) < 1000:
                for i in range(1, 2000):
                    if num % i == 0:
                        PrimeList.append(num)
                print(PrimeList)
        else:
            print(args.N)
    else:
        f0 = 0
        f1 = 1
        while args.N > 0:
            a = a
        print('fibonacci')
else:
    print('Wrong input')
    exit()