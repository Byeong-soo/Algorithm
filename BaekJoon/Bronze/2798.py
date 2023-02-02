import sys


if __name__ == '__main__':
    card_count, target_num = map(int, sys.stdin.readline().rstrip().split(" "))
    card_num = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    pick = [False for x in range(card_count)]
    answer = []
    sum_pick = 0

    for i in range(card_count):
        pick[i] = True
        for j in range(i+1, card_count):
            pick[j] = True
            for k in range(j+1, card_count):
                pick[k] = True
                if sum([card_num[x] for x in range(card_count) if pick[x]]) <= target_num:
                    answer.append(sum([card_num[x] for x in range(card_count) if pick[x]]))
                pick[k] = False
            pick[j] = False
        pick[i] = False

    print(max(answer))
