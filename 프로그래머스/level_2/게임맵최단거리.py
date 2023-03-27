import collections


def solution(maps):
    answer = 0
    maps_x_size = len(maps[0])
    maps_y_size = len(maps)

    count = [[float("inf") for _ in range(maps_x_size)] for _ in range(maps_y_size)]
    deque = collections.deque([])

    count[0][0] = 1
    deque.append([0, 0, 1])

    while deque:

        popleft = deque.popleft()

        direction_x = [1, -1, 0, 0]
        direction_y = [0, 0, 1, -1]

        for i in range(4):
            new_x = popleft[1] + direction_x[i]
            new_y = popleft[0] + direction_y[i]

            if not (0 <= new_x < maps_x_size and 0 <= new_y < maps_y_size):
                continue
            if maps[new_y][new_x] == 0:
                continue
            if count[new_y][new_x] > popleft[2] + 1:
                count[new_y][new_x] = popleft[2] + 1
                deque.append([new_y, new_x, count[new_y][new_x]])
    answer = count[maps_y_size-1][maps_x_size-1]
    if answer == float("inf"):
        answer = -1

    return answer


if __name__ == '__main__':
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))
