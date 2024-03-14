n = int(input())
result = 666
cnt = 0
while cnt < (n - 1):
    result += 1
    if str(result).count("666"):
        cnt += 1

print(result)