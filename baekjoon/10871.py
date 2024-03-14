import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))

result = list(filter(lambda d : d < x, a))
for i in result:
    print(i, end=" ")