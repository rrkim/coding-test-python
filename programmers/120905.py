def solution(n, numlist):
    return list(filter(lambda x: x%n == 0, numlist))

print(solution(5, [1, 9, 3, 10, 13, 5]))