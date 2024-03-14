import sys

input = sys.stdin.readline

n = int(input())
if n%2 == 0:
    result = "even"
else:
    result = "odd"

print("{} is {}".format(n, result))