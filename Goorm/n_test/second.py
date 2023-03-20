import collections
import sys


def change_new_format(origin_list):
    target = ""
    temp_num = 0
    change_list = []
    for origin in origin_list:
        if origin != target:
            target = origin
            change_list.append(temp_num)
            temp_num = 1
        else:
            temp_num += 1
    change_list.append(temp_num)
    return int("".join(map(str, change_list)))


if __name__ == '__main__':
    origin_sencer, latest_sencer = map(int, sys.stdin.readline().rstrip().split(" "))
    origin_list = list(sys.stdin.readline().rstrip().split(" "))
    latest_list = list(sys.stdin.readline().rstrip().split(" "))
    visited = []
    target = "".join(latest_list)
    answer = 0
    find = False

    deque = collections.deque([(origin_list, 0)])

    while deque:
        pop_info = deque.popleft()
        pop = pop_info[0]
        count = pop_info[1]

        for i in range(len(pop)):
            if i == 0:
                continue
            if pop[i] != pop[i - 1]:
                temp = pop[i]
                pop[i] = pop[i - 1]
                pop[i - 1] = temp
                if change_new_format(pop) not in visited:
                    check = str(change_new_format(pop))
                    if check == target:
                        print(pop)
                        find = True
                        answer = count + 1
                        break
                    visited.append(check)
                    new_list = pop[:]
                    deque.append((new_list, count + 1))
                temp = pop[i]
                pop[i] = pop[i - 1]
                pop[i - 1] = temp
        if find:
            break
    print(answer)
