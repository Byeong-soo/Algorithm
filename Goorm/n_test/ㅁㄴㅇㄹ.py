import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

old_sensor_list = list(map(int, input().split()))
new_sensor_list = list(map(int, input().split()))

old_sensor_q = deque(old_sensor_list)

now_value = None
now_count = 0
remain_value_list = []
new_sensor_idx = 0
answer = 0

while old_sensor_q:
    print("—————")
    print(old_sensor_q)
    # print(remain_value_list)
    # print(now_value)
    # print(answer)
    sensor = old_sensor_q.popleft()
    print("sensor", sensor)
    if not now_value:
        now_value = sensor


    if sensor == now_value:
        print("doit")
        now_count += 1
    else:
        print("else")
        answer += len(remain_value_list)
        remain_value_list.append(sensor)

    print("now_value", now_value)
    print("count", now_count)

    if now_count == new_sensor_list[new_sensor_idx]:
        new_sensor_idx += 1
        while remain_value_list:
            old_sensor_q.appendleft(remain_value_list.pop())
        now_count = 0
        now_value = None


print(answer)
