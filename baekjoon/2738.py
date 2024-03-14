matrix_a, matrix_b = [], []
m, n = map(int, input().split())

for _ in range(m):
    temp = list(map(int, input().split()))
    matrix_a.append(temp)

for _ in range(m):
    temp = list(map(int, input().split()))
    matrix_b.append(temp)

for i in range(m):
    for k in range(n):
        print(matrix_a[i][k] + matrix_b[i][k], end=" ")
    print()