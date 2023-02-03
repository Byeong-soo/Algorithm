import sys

if __name__ == '__main__':
    lecture_count, disk_count = map(int, sys.stdin.readline().rstrip().split(" "))
    lecture_size_map = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    max_size = max(lecture_size_map)

    size_sum = sum(lecture_size_map)
    start = 0
    end = size_sum
    minimum = float("inf")
    while start <= end:
        mid = (start + end) // 2
        present_count = disk_count
        present_size = mid
        possible = True

        if mid >= max_size:
            for i in lecture_size_map:
                if present_size < i:
                    if present_count > 1:
                        present_size = mid
                        present_size -= i
                        present_count -= 1
                    else:
                        possible = False
                        break
                else:
                    present_size -= i
        else:
            possible = False
        if possible and minimum > mid:
            minimum = mid

        if possible:
            end = mid
            end -= 1
        else:
            start = mid
            start += 1

    print(minimum)
