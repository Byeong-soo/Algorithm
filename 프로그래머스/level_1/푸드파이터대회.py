import collections


def solution(food):
    answer = ''
    answer_list = []
    deque = collections.deque([])

    for i in range(1,len(food)):
        count = food[i] // 2
        for j in range(count):
            answer_list.append(i)
            deque.appendleft(i)

    answer_list.append(0)
    answer = answer_list + list(deque)
    answer = "".join(map(str,answer))

    return answer
