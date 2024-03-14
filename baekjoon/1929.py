import sys

def is_prime(n):
    if n == 1 or n == 2:
        return False

    for i in range(2, n-1):
        if (n%i) == 0:
            return False

    return True

input = sys.stdin.readline
M, N = map(int, input().split())
for n in range(M, N+1):
    if is_prime(n):
        print(n)