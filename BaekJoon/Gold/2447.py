import sys


def draw(count):
    if count == 0:
        return [
            "*"
        ]

    result = []

    for row in draw(count - 1):
        result.append(row * 3)

    for row in draw(count - 1):
        result.append((row + " " * 3 ** (count - 1) + row))

    for row in draw(count - 1):
        result.append(row * 3)

    return result


if __name__ == '__main__':
    input = int(sys.stdin.readline().rstrip())

    depth = 0

    while input != 1:
        depth += 1
        input /= 3

    result_list = draw(depth)

    for result in result_list:
        print(result)
