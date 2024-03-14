def solution(n, control):
    word = {"w": 1, "s": -1, "d": 10, "a": -10}
    for s in control:
        n += word[s]

    return n

print(solution(0, "wsdawsdassw"))