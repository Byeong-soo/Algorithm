def solution(s):
    answer = ''
    s = s.lower()
    string_list = str(s).split(" ")
    print(string_list)
    temp = []

    for word in string_list:
        word_list = list(word)
        if word_list:
            word_list[0] = word_list[0].upper()
        word = "".join(word_list)
        temp.append(word)

    answer = " ".join(temp)
    return answer

if __name__ == '__main__':
    print(solution("3people  unFollowed me"))
