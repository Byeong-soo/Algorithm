import sys

if __name__ == '__main__':
    first_num = int(sys.stdin.readline().rstrip())
    result = 0
    for i in range(first_num):
        present_num = i
        sum = present_num
        while present_num > 0:
            sum += present_num % 10
            present_num = present_num//10
        if sum == first_num:
            result = i
            break

    print(result)

