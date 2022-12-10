# 충격...

def mark_x_y(x,y):
    for i in range(count):
        chessboard[count-1][x] = 1

    for i in range(count):
        chessboard[y][count-1] = 1

    # for i in range(count):
    #     if x+1 >= count or y+1 >= count:
    #         break
    #     chessboard[x+1][y+1] = 1
    # for i in range(count):
    #     if x-1 <= 0 or y-1 <= 0:
    #         break
    #     chessboard[x-1][y-1] = 1


if __name__ == '__main__':
    count = int(input())
    chessboard = [[0 for x in range(count)] for y in range(count)]

    mark_x_y(2,3)

    for i in range(count):
        print()
        for u in range(count):
            print(chessboard[i][u],end=" ")