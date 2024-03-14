def solution(numbers, n):
    answer, cnt = 0, 0
    while answer <= n:
        answer += numbers[cnt]
        cnt += 1

    return answer

print(solution([58, 44, 27, 10, 100], 139))