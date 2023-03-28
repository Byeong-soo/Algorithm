import collections


def solution2(x, y, n):
    answer = float("inf")
    deque = collections.deque([(x, 0)])

    while deque:
        popleft = deque.popleft()
        if popleft[0] + n < y:
            deque.append((popleft[0] + n, popleft[1] + 1))
        elif popleft[0] + n == y:
            answer = min(answer, popleft[1] + 1)
        if popleft[0] * 2 < y:
            deque.append((popleft[0] * 2, popleft[1] + 1))
        elif popleft[0] * 2 == y:
            answer = min(answer, popleft[1] + 1)
        if popleft[0] * 3 < y:
            deque.append((popleft[0] * 3, popleft[1] + 1))
        elif popleft[0] * 3 == y:
            answer = min(answer, popleft[1] + 1)

    if answer == float("inf"):
        return -1
    return answer


def solution(x, y, n):
    if x == y:
        return 0

    dp = [float('inf')] * (y + 1)
    dp[x] = 0

    for i in range(x, y + 1):
        if dp[i] == float('inf'):
            continue

        if i + n <= y:
            dp[i + n] = min(dp[i + n], dp[i] + 1)

        if i * 2 <= y:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)

        if i * 3 <= y:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)

    if dp[y] == float('inf'):
        return -1

    return dp[y]


if __name__ == '__main__':
    print(solution(10, 40, 5))
    print(solution(10, 40, 30))
    print(solution(2, 5, 4))
