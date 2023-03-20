import collections


def bfs(h, w):
    visited[h][w] = True
    total_sum = 0
    queue = []
    if total_map[h][w] != "X":
        queue = collections.deque([(h, w)])
        total_sum += int(total_map[h][w])

    while queue:

        direction_x = [1, -1, 0, 0]
        direction_y = [0, 0, 1, -1]

        pop = queue.pop()
        pop_h, pop_w = pop[0], pop[1]
        for i in range(4):
            change_w = pop_w + direction_x[i]
            change_h = pop_h + direction_y[i]
            if change_h < 0 or change_h >= y_size:
                continue
            if change_w < 0 or change_w >= x_size:
                continue

            if not visited[change_h][change_w]:
                if total_map[change_h][change_w] != "X":
                    visited[change_h][change_w] = True
                    queue.append((change_h, change_w))
                    total_sum += int(total_map[change_h][change_w])
    return total_sum

def solution(maps):
    global visited, y_size, x_size, total_map
    answer = []
    total_map = []

    for i in maps:
        total_map.append(list(i))

    y_size = len(maps)
    x_size = len(total_map[0])

    visited = [[False for _ in range(x_size)] for _ in range(y_size)]

    for w in range(x_size):
        for h in range(y_size):
            if not visited[h][w]:
                return_value = bfs(h, w)
                if return_value is not None and return_value != 0:
                    answer.append(return_value)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer


if __name__ == '__main__':
    solution(["X591X", "X1X5X", "X231X", "1XXX1"])
