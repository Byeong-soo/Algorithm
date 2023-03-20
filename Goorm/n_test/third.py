import collections
import sys


def bfs(height, width):
    visited[height][width] = True
    deque = []
    bird_count = 0
    drone_count = 0

    if total_map[height][width] != "#":
        deque = collections.deque([(height, width)])
        if total_map[height][width] == "v":
            bird_count += 1
        elif total_map[height][width] == "o":
            drone_count += 1

    while deque:
        direction_x = [1, -1, 0, 0]
        direction_y = [0, 0, 1, -1]

        pop = deque.pop()
        pop_h = pop[0]
        pop_w = pop[1]

        for i in range(4):
            change_w = pop_w + direction_x[i]
            change_h = pop_h + direction_y[i]
            if change_h < 0 or change_h >= y_size:
                continue
            if change_w < 0 or change_w >= x_size:
                continue

            if not visited[change_h][change_w]:
                visited[change_h][change_w] = True
                if total_map[change_h][change_w] != "#":
                    deque.append((change_h, change_w))
                    if total_map[change_h][change_w] == "o":
                        drone_count += 1
                    elif total_map[change_h][change_w] == "v":
                        bird_count += 1

    if drone_count <= bird_count:
        answer[1] += bird_count
    else:
        answer[0] += drone_count


if __name__ == '__main__':
    x_size, y_size = map(int, sys.stdin.readline().rstrip().split(" "))
    total_map = []
    for i in range(y_size):
        total_map.append(list(sys.stdin.readline().rstrip()))

    visited = [[False for _ in range(x_size)] for _ in range(y_size)]
    answer = [0, 0]
    for i in range(y_size):
        for j in range(x_size):
            if not visited[i][j]:
                bfs(i, j)

    print(" ".join(map(str, answer)))
