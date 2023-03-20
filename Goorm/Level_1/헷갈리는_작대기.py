import sys

if __name__ == '__main__':
    words = list(sys.stdin.readline().rstrip())
    result = [0, 0, 0, 0]
    for word in words:
        if word == "1":
            result[0] += 1
        elif word == "I":
            result[1] += 1
        elif word == "l":
            result[2] += 1
        elif word == "|":
            result[3] += 1
    print("\n".join(map(str,result)))
