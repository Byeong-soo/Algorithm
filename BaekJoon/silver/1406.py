import collections
import sys

if __name__ == '__main__':

    cursor_left = (list(sys.stdin.readline().rstrip()))
    cursor_right = collections.deque([])
    order_count = int(sys.stdin.readline().rstrip())
    left_length = len(cursor_left)
    right_length = len(cursor_right)

    for i in range(order_count):
        order = (sys.stdin.readline().rstrip())
        if order == "L":
            if left_length != 0:
                left_length -= 1
                right_length += 1
                pop = cursor_left.pop()
                cursor_right.appendleft(pop)
        elif order == "D":
            if right_length != 0:
                left_length += 1
                right_length -= 1
                popleft = cursor_right.popleft()
                cursor_left.append(popleft)
        elif order == "B":
            if left_length != 0:
                left_length -= 1
                cursor_left.pop()
        else:
            order = list(order)
            cursor_left.append(order[2])
            left_length += 1

    sum_str = cursor_left + list(cursor_right)
    print("".join(sum_str))

