# https://school.programmers.co.kr/learn/courses/30/lessons/84512
import itertools


# A E I O U
def solution(word):
    answer = 0
    word_list = ["A", "E", "I", "O", "U"] * 5
    word_all_set = set([])
    word_all_list = []
    for i in range(1, 6):
        permutations = itertools.permutations(word_list, i)
        for find_word in permutations:
            word_all_set.add("".join(find_word))
            # word_all_list.append("".join(find_word))
    word_all_list = list(word_all_set)
    word_all_list.sort()

    for i in range(len(word_all_list)):
        if word_all_list[i] == word:
            answer = i + 1

    return answer


if __name__ == '__main__':
    print(solution("AAAAE"))
    print(solution("AAAE"))
    print(solution("I"))
    print(solution("EIO"))
