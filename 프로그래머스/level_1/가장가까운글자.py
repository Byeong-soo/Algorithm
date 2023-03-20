def solution(s):
    position = [-1 for _ in range(26)]
    word_list = list(s)
    answer = []

    for word in range(len(word_list)):
        temp_position = ord(word_list[word]) % 97
        if position[temp_position] == -1:
            answer.append(-1)
        else:
            answer.append(word - position[temp_position])
        position[temp_position] = word

    return answer


if __name__ == '__main__':
    solution("foobar")
