def solution(arr):
    for i in range(len(arr)):
        n = arr[i]
        if n >= 50 and n % 2 == 0:
            arr[i] //= 2
        elif n < 50 and n % 2 != 0:
            arr[i] *= 2

    return arr

print(solution([1,2,3,100,99,98]))