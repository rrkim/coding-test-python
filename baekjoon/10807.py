import sys

n = int(sys.stdin.readline().rstrip())
a = list(map(int, sys.stdin.readline().rstrip().split()))
v = int(sys.stdin.readline().rstrip())

print(a.count(v))