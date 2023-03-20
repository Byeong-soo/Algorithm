import itertools


def solution(number):
    num_list = list(itertools.combinations(number, 3))
    answer = 0

    for nums in num_list:
        if sum(nums) == 0:
            answer += 1
    return answer


if __name__ == '__main__':
    print(solution([-1, 1, -1, 1]))
