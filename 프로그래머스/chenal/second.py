import collections


def solution(gold_prices):
    answer = 0
    index = 0
    deque = collections.deque([])
    deque.append((index + 1, gold_prices[index], 0, True))
    deque.append((index + 1, 0, 0, False))
    max_value = [0 for _ in range(len(gold_prices))]

    while deque:
        index, buy_value, sum_value, have_gold = deque.popleft()
        if index >= len(gold_prices):
            continue

        if have_gold:
            if max_value[index] < max_value[index] + gold_prices[index] - buy_value:
                deque.append((index + 2, 0, sum_value + gold_prices[index] - buy_value, False))
                max_value[index:] = [
                    max(max_value[index] + gold_prices[index] - buy_value, sum_value + gold_prices[index] - buy_value)
                    for _ in
                    range(len(max_value) - index)]
        else:
            deque.append((index + 1, gold_prices[index], sum_value, True))
    answer = max(max_value)
    return answer


if __name__ == '__main__':
    print(solution([2, 5, 1, 3, 4]))
    print(solution([7, 2, 5, 6, 1, 4, 2, 8]))
