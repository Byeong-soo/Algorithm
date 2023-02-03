import sys

if __name__ == '__main__':
    mine_card_count = int(sys.stdin.readline())
    mine_card_list = list(map(int, sys.stdin.readline().rstrip().split(" ")))

    check_card_count = int(sys.stdin.readline())
    check_card_list = list((map(int, sys.stdin.readline().rstrip().split(" "))))

    result = dict.fromkeys(check_card_list, "0")
    check_card_list = sorted(check_card_list)
    for num in range(mine_card_count):

        start = 0
        end = check_card_count - 1

        while start <= end:
            mid = (start + end) // 2

            if check_card_list[mid] > mine_card_list[num]:
                end = mid
                end -= 1
            elif check_card_list[mid] < mine_card_list[num]:
                start = mid
                start += 1
            else:
                result[check_card_list[mid]] = "1"
                break
    print(" ".join(result.values()))
    # print("".join(result))
