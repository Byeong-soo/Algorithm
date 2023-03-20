import sys

if __name__ == '__main__':
    size = int(sys.stdin.readline().rstrip())
    dp = [[] for _ in range(size)]
    number_list = []

    for i in range(size):
        numbers = sys.stdin.readline().rstrip().split()
        number_list.append(numbers)

    for i in range(size - 1):
        for j in range(i + 1):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + number_list[i + 1][j])

    print(number_list)
    print(dp)
