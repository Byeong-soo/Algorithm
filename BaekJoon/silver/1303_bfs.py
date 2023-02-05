import collections
import sys


def bfs(w, h):
    global data, score
    target = data[h][w]
    visited[h][w] = True
    count = 1
    queue = collections.deque([(h, w)])

    while queue:

        direction_x = [1, -1, 0, 0]
        direction_y = [0, 0, 1, -1]

        pop = queue.pop()
        pop_h, pop_w = pop[0], pop[1]
        for i in range(4):
            change_w = pop_w + direction_x[i]
            change_h = pop_h + direction_y[i]
            if change_h < 0 or change_h >= height:
                continue
            if change_w < 0 or change_w >= width:
                continue

            if not visited[change_h][change_w]:
                if data[change_h][change_w] == target:
                    visited[change_h][change_w] = True
                    queue.append((change_h, change_w))
                    count += 1
    if target == "W":
        score[0] += count ** 2
    else:
        score[1] += count ** 2


if __name__ == '__main__':
    width, height = map(int, sys.stdin.readline().rstrip().split(" "))
    data = []
    visited = []
    score = [0, 0]

    for i in range(height):
        data.append(list(sys.stdin.readline().rstrip()))
        visited.append([False for _ in range(width)])

    for w in range(width):
        for h in range(height):
            if not visited[h][w]:
                bfs(w, h)

    print(" ".join(map(str, score)))
