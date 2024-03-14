n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append([True for _ in range(n)])

for i in range(m):
    a, b = sorted(list(map(int, input().split())))
    arr[a-1][b-1] = False

cnt = 0
for i in range(0, n):
    for k in range(i+1, n):
        for j in range(k+1, n):
            if arr[i][k] and arr[i][j] and arr[k][j]:
                cnt += 1

print(cnt)