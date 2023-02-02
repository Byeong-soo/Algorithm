import sys

if __name__ == '__main__':
    str_length = int(sys.stdin.readline().rstrip())
    str_list = list(sys.stdin.readline().rstrip())
    result = 0
    temp = 0
    number_count = 0
    for i in range(str_length - 1, -1, -1):
        try:
            temp += (10 ** number_count) * (int(str_list[i]))
            number_count += 1
        except ValueError:
            if number_count < 7:
                result += temp
            number_count = 0
            temp = 0

    if number_count < 7:
        result += temp
    print(result)
