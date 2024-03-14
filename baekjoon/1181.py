
cnt = int(input())
list = []
for i in range(cnt):
    list.append(input())

list = sorted(set(list), key=lambda d: (len(d), d))
print(*list, sep="\n", end="")