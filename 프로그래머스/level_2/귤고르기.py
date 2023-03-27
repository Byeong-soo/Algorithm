import collections


def solution(k, tangerine):
    answer = 0
    count = [0 for _ in range(10000000)]

    for num in tangerine:
        count[num] += 1

    count.sort(reverse=True)

    for x in range(len(count)):
        if count[x] > 0:
            k -= count[x]
            answer += 1
            if k <= 0:
                break
        else:
            break

    return answer


if __name__ == '__main__':
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
