import collections
import sys

if __name__ == '__main__':
    count = int(sys.stdin.readline().rstrip())
    building = [[] for x in range(count + 1)]
    indegree_count = [0 for x in range(count + 1)]
    cost = [0 for x in range(count + 1)]
    result = [0 for x in range(count + 1)]

    for i in range(1, count + 1):
        build_info = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        cost[i] = build_info[0]
        building_info = build_info[1:-1]

        for j in building_info:
            building[j].append(i)
            indegree_count[i] += 1

    deque = collections.deque([])

    for i in range(1, count + 1):
        if indegree_count[i] == 0:
            deque.append(i)

    while deque:
        popleft = deque.popleft()

        result[popleft] += cost[popleft]
        for b in building[popleft]:
            indegree_count[b] -= 1
            result[b] = max(result[b], result[popleft])
            if indegree_count[b] == 0:
                deque.append(b)

    print("\n".join((map(str, result[1:]))))
