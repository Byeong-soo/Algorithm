import sys

if __name__ == '__main__':
    first_count, second_count = map(int, sys.stdin.readline().rstrip().split(" "))
    first_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    second_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    sum_list = first_list + second_list
    sum_list.sort()
    print(" ".join(map(str,sum_list)))
