# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3
import collections
import itertools


def check_num(number):
    if number == 1 or number == 0:
        return False
    num = int(number ** 0.5)

    for i in range(2, num + 1):
        if number % i == 0:
            return False
    return True


def solution(numbers):
    global num_set
    global num_list
    answer = 0
    num_list = list(numbers)
    num_set = set([])
    for num in range(len(num_list)):
        visited = [False for _ in range(len(num_list))]
        visited[num] = True
        make_num([num_list[num]], 1, visited)

    for num in num_set:
        if check_num(num):
            answer+=1
    return answer


def make_num(num, count, visited):
    deque = collections.deque([(num, count, visited)])

    while deque:
        pop_number, pop_count, pop_visited = deque.popleft()
        num_set.add(int("".join(pop_number)))

        for i in range(len(num_list)):
            if pop_visited[i]:
                continue
            else:
                new_number = list(pop_number)
                new_number.append(num_list[i])
                new_visited = list(pop_visited)
                new_visited[i] = True
                deque.append(((new_number),pop_count+1,new_visited))


def solution(numbers):
    answer = 0
    num_list = list(numbers)
    num_set2 = set()
    for size in range(1, len(num_list) + 1):
        num_set = set(itertools.permutations(num_list, size))
        for num in num_set:
            num_set2.add(int("".join(num)))

    for num in num_set2:
        if check_num(int(num)):
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution("17"))
    print(solution("011"))
    print(solution("1231"))
