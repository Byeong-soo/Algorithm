import collections
import sys

if __name__ == '__main__':
    left_str = list(sys.stdin.readline().rstrip())
    boom_str = sys.stdin.readline().rstrip()
    boom_str_len = len(boom_str)
    right_str = []

    for i in left_str:
        right_str.append(i)
        if len(right_str) >= boom_str_len:
            if "".join(right_str[-boom_str_len:]) == boom_str:
                for _ in range(boom_str_len):
                    right_str.pop()

    if len(right_str) == 0:
        print("FRULA")
    else:
        print("".join(right_str))


