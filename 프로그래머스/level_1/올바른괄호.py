def is_correct_parenthesis(string):
    string_list = list(string)

    open_count = 0
    left_count = 0
    right_count = 0
    while string_list:
        pop = string_list.pop()

        if pop == "(":
            if open_count <= 0:
                return False
            open_count -= 1
            left_count += 1
        elif pop == ")":
            open_count += 1
            right_count += 1

    if left_count == right_count and open_count == 0:
        return True
    return False


if __name__ == '__main__':
    print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
    print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
    print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
    print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
    print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))
    # ")" 가 있어야 "("가 나올수 있음
