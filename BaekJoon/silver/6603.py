import itertools
import sys

if __name__ == '__main__':
    count = 0
    while True:
        numbers = list(map(int, sys.stdin.readline().rstrip().split(" ")))

        if numbers[0] == 0:
            break
        if count != 0:
            print("")

        combinations = list(itertools.combinations(numbers[1:], 6))

        for combination in combinations:
            print(" ".join(map(str, sorted(combination))))

        count += 1
