import collections
import sys

if __name__ == '__main__':
    target = int(sys.stdin.readline().rstrip())
    visited = [[False for _ in range(target + 1)] for _ in range(target + 1)]
    # screen, count, time
    deque = collections.deque([(1, 0, 0)])

    while deque:

        pop_info = deque.popleft()
        screen = pop_info[0]
        count = pop_info[1]
        time = pop_info[2]

        if screen == target:
            print(time)
            break

        if screen != 0:
            deque.append((screen, screen, time + 1))
        if count != 0 and target >= count:
            if screen + count <= target and not visited[screen + count][count]:
                deque.append((screen + count, count, time + 1))
                visited[screen + count][count] = True
        if screen > 0 and target >= count:
            if count != 0 and screen > 1 and not visited[screen - 1][count]:
                deque.append((screen - 1, count, time + 1))
                visited[screen - 1][count] = True
