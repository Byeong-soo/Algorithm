import itertools
import sys

if __name__ == '__main__':
    target_num = int(sys.stdin.readline().rstrip())
    result_list = [str(x + 1) for x in range(target_num)]
    number_list = list(itertools.permutations(result_list))
    for numbers in number_list:
        print(" ".join(numbers))
