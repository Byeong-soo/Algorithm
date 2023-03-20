import sys

if __name__ == '__main__':
    people_num, charge_time = map(int, sys.stdin.readline().rstrip().split(" "))
    people_list = []
    total_time = 0
    for i in range(people_num):
        people_list.append(list(map(int, sys.stdin.readline().rstrip().split(" "))))
    people_list.sort()

    for i in range(people_num):
        if i == 0:
            total_time += people_list[i][0] + people_list[i][1]
        else:
            if total_time < people_list[i][0]:
                total_time = people_list[i][0] + people_list[i][1]
            else:
                total_time += people_list[i][1]
        total_time += charge_time
    print(total_time)
