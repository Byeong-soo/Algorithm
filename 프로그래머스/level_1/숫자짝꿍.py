def solution(X, Y):
    first_number_list = list(X)
    second_number_list = list(Y)
    list_ = []
    # second_number_list.sort(reverse=True)
    first_count = [0 for _ in range(10)]
    second_count = [0 for _ in range(10)]

    for i in range(len(first_number_list)):
        first_count[int(first_number_list[i])] += 1
    for i in range(len(second_number_list)):
        second_count[int(second_number_list[i])] += 1

    answer = ""
    for i in range(9, -1, -1):
        count = min(first_count[i], second_count[i])
        answer += str(i) * count

    if answer == "":
        answer = "-1"
    else:
        answer = str(int(answer))
    return answer


if __name__ == '__main__':
    print(solution("5525", "1255"))
