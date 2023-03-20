import math


def solution(progresses, speeds):
    answer = []
    time = []

    stack_count = 0
    stack_day = 0

    while progresses:
        progress = progresses.pop()
        speed = speeds.pop()

        need_progress = 100 - progress
        need_time = math.ceil(need_progress / speed)

        if need_time <= stack_day:
            stack_count += 1
            time.append(stack_count)
            stack_count = 0
        elif need_time > stack_day:
            stack_count+=1
            stack_day = need_time
    return time


if __name__ == '__main__':
    print(solution([93, 30, 55], [1, 30, 5]))
