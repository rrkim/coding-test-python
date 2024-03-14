def solution(n):
    if n % 2 == 0:
        answer = 0
        for i in (range(2, n + 1, 2)):
            answer += i ** 2
        return answer

    return sum(list(range(1, n + 1, 2)))

print(solution(10))