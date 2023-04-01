# https://school.programmers.co.kr/learn/courses/30/lessons/159993
import collections


def find(y, x, target):
    deque = collections.deque([])
    deque.append((y, x, 0))
    direction_x = [1, -1, 0, 0]
    direction_y = [0, 0, 1, -1]
    visited[y][x] = 0

    while deque:
        pop_y, pop_x, pop_count = deque.popleft()

        for i in range(4):
            change_y = direction_y[i] + pop_y
            change_x = direction_x[i] + pop_x

            if change_x >= x_size or change_x < 0:
                continue
            if change_y >= y_size or change_y < 0:
                continue

            if new_maps[change_y][change_x] == "X":
                continue
            if new_maps[change_y][change_x] == target:
                return pop_count + 1
            if new_maps[change_y][change_x] == "O" or (new_maps[change_y][change_x] == "E" ) or (new_maps[change_y][change_x] == "S"):
                if visited[change_y][change_x] > pop_count + 1:
                    deque.append((change_y, change_x, pop_count + 1))
                    visited[change_y][change_x] = pop_count + 1
    return -1


def solution(maps):
    answer = 0
    global x_size
    global y_size
    global new_maps, visited
    y_size = len(maps)

    for i in range(y_size):
        maps[i] = list(maps[i])

    new_maps = maps
    x_size = len(maps[0])
    visited = [[float("inf") for _ in range(x_size)] for _ in range(y_size)]
    to_l = 0
    to_e = 0
    for y in range(y_size):
        for x in range(x_size):
            if maps[y][x] == "S":
                to_l = find(y, x, "L")
                if to_l == -1:
                    return -1
    visited = [[float("inf") for _ in range(x_size)] for _ in range(y_size)]
    for y in range(y_size):
        for x in range(x_size):
            if maps[y][x] == "L":
                to_e = find(y, x, "E")
                if to_e == -1:
                    return -1

    answer = to_l + to_e
    return answer


if __name__ == '__main__':
    print(solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"]))
    print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
    print(solution(["SOOOO", "XXXXX", "LOOOO", "XXXXX", "EOOOO"]))
