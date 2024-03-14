n = input()
total = int(n)
data = list(n)
cnt = 0

while total > 9:
    cnt += 1
    total = 0
    for i in data:
        total += int(i)

    data = list(str(total))

print(cnt)
print("NO" if (total%3) else "YES")
