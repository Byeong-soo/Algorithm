# https://school.programmers.co.kr/learn/courses/30/lessons/43165
import collections


def solution(numbers, target):
    answer = 0
    result_list = []

    pop = numbers.pop()
    result_list.append(pop)
    result_list.append(-pop)
    for num in numbers:
        temp = []
        while result_list:
            result = result_list.pop()
            temp.append(result + num)
            temp.append(result - num)
        result_list = list(temp)
    for num in result_list:
        if target == num:
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))
