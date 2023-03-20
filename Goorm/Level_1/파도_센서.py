import sys

if __name__ == '__main__':
    wave_x, wave_y, wave_r = map(int, sys.stdin.readline().rstrip().split(" "))
    sencer_distance = []

    for _ in range(5):
        sencer_x, sencer_y = map(int,sys.stdin.readline().rstrip().split(" "))
        sencer_distance.append((abs(wave_x - sencer_x) **2 + abs(wave_y - sencer_y) ** 2) ** 0.5)

    min_distance_sencer = min(range(len(sencer_distance)),key=sencer_distance.__getitem__) + 1
    min_distance = min(sencer_distance)
    if wave_r < min_distance:
        print(-1)
    else:
        print(min_distance_sencer)






