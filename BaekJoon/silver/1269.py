import sys

if __name__ == '__main__':
    first_count, second_count = map(int, sys.stdin.readline().rstrip().split(" "))
    first_list = set(sys.stdin.readline().rstrip().split(" "))
    second_list = set(sys.stdin.readline().rstrip().split(" "))

    sum_list = (first_list | second_list)
    print(len(sum_list) * 2 - first_count - second_count)
