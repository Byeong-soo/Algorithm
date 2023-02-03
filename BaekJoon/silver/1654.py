import sys

if __name__ == '__main__':
    have_line_count, target_count = map(int, sys.stdin.readline().rstrip().split(" "))
    line_list = []
    for _ in range(have_line_count):
        line_list.append(int(sys.stdin.readline().rstrip()))

    start = 1
    end = max(line_list)
    line_max = 0

    while start <= end:

        mid = (start + end) // 2

        count = 0
        for line in line_list:
            if mid != 0:
                count += line // mid

        if target_count > count:
            end = mid
            end -= 1
        elif target_count <= count:
            start = mid
            start += 1
            if line_max < mid:
                line_max = mid
    print(line_max)
