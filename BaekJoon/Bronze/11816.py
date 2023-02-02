import sys


def change_number(str):
    try:
        return int(str)
    except Exception:
        numbers = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
        return numbers[str]


if __name__ == '__main__':
    str_number = list(sys.stdin.readline().rstrip())

    if str_number[0] != "0":
        print(''.join(str_number))
    elif str_number[1] != "x":
        temp = 0
        for i in range(len(str_number)-1, 0, -1):
            temp += 8 ** (len(str_number)-1 - i) * change_number(str_number[i])
        print(temp)
    else:
        temp = 0
        for i in range(len(str_number)-1, 1, -1):
            temp += 16 ** (len(str_number)-1 - i) * change_number(str_number[i])
        print(temp)
