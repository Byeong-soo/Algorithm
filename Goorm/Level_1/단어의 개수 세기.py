import sys

if __name__ == '__main__':
    # words = list(set([x.lower() for x in (sys.stdin.readline().strip().split(" "))]))
    words = list(sys.stdin.readline().strip().split())
    print(len(words))
