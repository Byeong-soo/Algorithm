import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline())
    numbers = map(int, list(sys.stdin.readline().rstrip()))
    print(sum(numbers))
