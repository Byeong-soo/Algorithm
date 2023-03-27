# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# def solution(priorities, location):
#     answer = 0
#
#     new_list = []
#
#     for i in range(len(priorities)):
#         new_list.append((priorities[i],i))
#
#     new_list.sort(key=lambda e: (-e[0], e[1]))
#
#     for order in range(len(new_list)):
#         if location == new_list[order][1]:
#             answer = order + 1
#             break
#     return answer

def solution(priorities, location):
    n = len(priorities)
    t = 0
    for i in range(n):
        while priorities[t % n] == 0 or priorities[t % n] < max(priorities):
            t += 1
        if t % n == location:
            return i + 1
        priorities[t % n] = 0


if __name__ == '__main__':
    print(solution([2, 1, 3, 2], 2))
    print(solution([1, 1, 9, 1, 1, 1], 0))
