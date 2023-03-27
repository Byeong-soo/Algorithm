def solution(n, lost, reserve):
    answer = 0

    lost_1 = set(lost) - set(reserve)
    reserve_1 = set(reserve) - set(lost)

    lost_count = len(lost_1)
    answer = n - lost_count

    for i in reserve_1:
        for j in lost_1:
            if i + 1 == j or i - 1 == j:
                lost_1.remove(j)
                answer+=1
                break

    # for i in range(lost_count):
    #     for re in reserve:
    #         if lost[i] +1 == re or lost[i] -1 == re:
    #             reserve.remove(re)
    #             answer += 1
    #             break

    return answer


if __name__ == '__main__':
    print(solution(5, [2, 4], [3]))
