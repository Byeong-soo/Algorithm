# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    search_list = list(S)
    search_dic = {}
    max_distance = -1

    for i in range(len(search_list) - 1):
        if search_list[i] + search_list[i + 1] in search_dic.keys():
            search_dic[search_list[i] + search_list[i + 1]] += [i]
        else:
            search_dic[search_list[i] + search_list[i + 1]] = [i]

    for value in search_dic.values():
        if len(value) > 1:
            distance = max(value) - min(value)
            if max_distance < distance:
                max_distance = distance

    return max_distance


if __name__ == '__main__':
    print(solution("aakmaakmakda"))
    print(solution("aaa"))
    print(solution("codility"))
