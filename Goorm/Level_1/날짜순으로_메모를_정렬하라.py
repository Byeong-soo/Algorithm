import sys
import re

if __name__ == '__main__':
    memo = ""
    memo_list = []
    while memo != "END":
        memo = sys.stdin.readline().rstrip()
        if memo == "END":
            break
        pattern = "(\\d{2,4})년[\\s]??(\\d{1,2})월[\\s]?(\\d{1,2})일"
        regex_result = re.search(pattern, memo)
        if regex_result is None:
            pattern = "(\\d{2,4})[-|.|\\s|/]?(\\d{1,2})[-|.|\\s|/]?(\\d{1,2})"
            regex_result = re.search(pattern, memo)

        result = regex_result.groups()
        day = [0,0,0]
        if len(result[0]) == 2:
            day[0] = "20" + result[0]
        else:
            day[0] = result[0]
        if len(result[1]) == 1:
            day[1] = "0" + result[1]
        else:
            day[1] = result[1]
        if len(result[2]) == 1:
            day[2] = "0" + result[2]
        else:
            day[2] = result[2]

        memo_list.append(["".join(day),memo])

    memo_list.sort()

    for memo_info in memo_list:
        print(memo_info[1])
