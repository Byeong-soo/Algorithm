import collections


def solution(s):
    word_list = list(s)
    deque = collections.deque(word_list)
    compare_word = ""
    my_count = 0
    other_count = 0
    answer = 0

    while deque:
        popleft = deque.popleft()
        if compare_word == "":
            my_count += 1
            compare_word = popleft
            continue
        if compare_word == popleft:
            my_count += 1
        elif compare_word != popleft:
            other_count += 1

        if other_count == my_count and compare_word != 0:
            compare_word = ""
            my_count = 0
            other_count = 0
            answer += 1
    if my_count != 0:
        answer += 1
    return answer


if __name__ == '__main__':
    print(solution("banana"))
