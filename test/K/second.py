# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    delete_count = []
    B_list = []
    A_count = 0
    B_count = 0
    min_value = float("inf")

    list_S = list(S)

    while list_S:
        pop = list_S.pop()
        if pop == "A":
            A_count += 1
        else:
            B_count += 1
            B_list.append((A_count, B_count))

    b_size = len(B_list)
    for i in range(b_size-1):
        cal_value = B_list[i][0] + (B_list[b_size-1][1] - B_list[i][1])
        if min_value > cal_value:
            min_value = cal_value

    if A_count == 0 or B_count == 0:
        return 0

    if B_list[b_size-1][0] < min_value:
        return B_list[b_size-1][0]

    return min_value

    # for i in range(len(S)):
    #     if S[i] == "A":
    #         A_count += 1
    #         for delete_info in delete_count:
    #             if delete_info[0] < i:
    #                 delete_info[1] += 1
    #     elif S[i] == "B":
    #         temp_delete_count = B_count
    #         delete_count.append([i, temp_delete_count])
    #         B_count += 1
    # if B_count == 0 or A_count == 0:
    #     return 0

    # return min(delete_count, key=lambda x: x[1])[1]


if __name__ == '__main__':
    print(solution("BAAABAB"))
    print(solution("BBABAA"))
    print(solution("AABBBB"))
    print(solution("A"))
