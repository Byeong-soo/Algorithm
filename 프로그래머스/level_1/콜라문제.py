def solution(need, b, n):
    empty = n
    answer = 0

    while empty >= need:
        get_bottle = empty // need
        empty = empty % need
        empty += get_bottle * b
        answer += get_bottle * b

    return answer
