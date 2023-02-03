import sys

if __name__ == '__main__':
    size = int(sys.stdin.readline().rstrip())
    target = int(sys.stdin.readline().rstrip())

    start = 1
    end = size ** 2

    while start < end:
        mid = (start + end) // 2
        count = 0
        for i in range(size):
            count += min(size, mid // (i + 1))

        if count < target:
            start
