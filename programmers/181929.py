def solution(num_list):
    sum_square = sum(num_list) ** 2
    multiply = 1
    for i in num_list:
        multiply *= i

    return int(multiply < sum_square)