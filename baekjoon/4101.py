
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0 and arr[1] == 0:
        break
    elif arr[0] > arr[1]:
        print("Yes")
    else:
        print("No")

