import itertools


def solution(nums):
    answer = 0
    size = len(nums) // 2
    num_set = set(nums)

    if len(num_set) > size:
        answer = size
    else:
        answer = len(num_set)
    return answer


if __name__ == '__main__':
    print(solution([3, 3, 3, 2, 2, 4]))
