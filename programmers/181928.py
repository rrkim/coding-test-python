def solution(num_list):
    answer = ["", ""]
    for i in num_list:
        answer[int(i % 2 == 0)] += str(i)

    return int(answer[0]) + int(answer[1])

print(solution([3, 4, 5, 2, 1]))