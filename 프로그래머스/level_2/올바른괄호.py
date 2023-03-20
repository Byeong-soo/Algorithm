def solution(s):

    bracket_list = list(s)

    left_count = 0
    right_count = 0
    open_count = 0

    while bracket_list:
        pop = bracket_list.pop()

        if pop == "(":
            if open_count == 0:
                return False
            else:
                open_count -= 1
                left_count += 1
        elif pop == ")":
            open_count += 1
            right_count += 1

    if open_count > 0 or left_count != right_count:
        return False

    return True


if __name__ == '__main__':
    print(solution("()()"))
