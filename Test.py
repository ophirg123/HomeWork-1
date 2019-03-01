import argparse

parser = argparse.ArgumentParser(description='Pi number for N digits, Nth prime number, Nth Fibonacci number')  # Parse Command-line argument
parser.add_argument('--task', type=str, required=True, help='type pi / prime / Fibonacci')
parser.add_argument('--N', type=int, required=True, help='Integer Number Between 1 and 1000')
args = parser.parse_args()

TaskList = ['pi','prime','Fibonacci']  # List of optional tasks
if args.task in TaskList and args.N in range(1, 1001):
    print('hello world')
else:
    print('Wrong input')
    exit()