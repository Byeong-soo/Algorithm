import collections
import copy
import sys

if __name__ == '__main__':
    height, width = map(int, sys.stdin.readline().rstrip().split(" "))
    map = []
    visited = [[[False, False] for _ in range(width)] for _ in range(height)]
    for _ in range(height):
        map.append(list(sys.stdin.readline().rstrip()))
    # position y,x,count,hammer
    visited[0][0][0] = True
    start = (0, 0, 1, 1)
    deque = collections.deque([start])
    result = -1
    while deque:
        pop_info = deque.popleft()
        pop_y = pop_info[0]
        pop_x = pop_info[1]
        pop_count = pop_info[2]
        pop_hammer = pop_info[3]

        if pop_x == width - 1 and pop_y == height - 1:
            result = pop_count
            break
        direction_x = [1, -1, 0, 0]
        direction_y = [0, 0, 1, -1]

        for i in range(4):
            change_y = pop_y + direction_y[i]
            change_x = pop_x + direction_x[i]

            if change_y < 0 or change_y >= height:
                continue
            if change_x < 0 or change_x >= width:
                continue

            if map[change_y][change_x] == "0":
                if pop_hammer > 0 and not visited[change_y][change_x][0]:
                    visited[change_y][change_x][0] = True
                    deque.append((change_y, change_x, pop_count + 1, pop_hammer))
                elif pop_hammer == 0 and not visited[change_y][change_x][1]:
                    visited[change_y][change_x][1] = True
                    deque.append((change_y, change_x, pop_count + 1, pop_hammer))

            if map[change_y][change_x] == "1":
                if pop_hammer > 0 and not visited[change_y][change_x][1]:
                    visited[change_y][change_x][1] = True
                    deque.append((change_y, change_x, pop_count + 1, pop_hammer - 1))
    print(result)
