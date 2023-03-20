import collections
import sys

if __name__ == '__main__':
    test_count = int(sys.stdin.readline().rstrip())

    for _ in range(test_count):
        team_count = int(sys.stdin.readline().rstrip())
        last_year = list(map(int, sys.stdin.readline().rstrip().split(" ")))
        indegree = [[] for _ in range(team_count)]
        indegree_count = [0 for _ in range(team_count)]
        this_year = []

        for x in range(1, team_count + 1):
            for y in range(team_count):
                if last_year[y] == x:
                    indegree[x - 1] = last_year[:-(team_count - y)]
                    indegree_count[x - 1] = y

        change_count = int(sys.stdin.readline().rstrip())
        result = True
        result_list = []
        deque = collections.deque([])
        for change in range(change_count):
            first, second = map(int, sys.stdin.readline().rstrip().split(" "))

            if first in indegree[second - 1]:
                indegree_count[first - 1] += 1
                indegree_count[second - 1] -= 1
                indegree[first - 1].append(second)
                indegree[second - 1].remove(first)
            elif second in indegree[first - 1]:
                indegree_count[first - 1] -= 1
                indegree_count[second - 1] += 1
                indegree[first - 1].remove(second)
                indegree[second - 1].append(first)

        for x in range(team_count):
            if indegree_count[x] == 0:
                deque.append(x)

        while deque:
            popleft = deque.popleft()
            result_list.append(popleft + 1)

            for x in range(team_count):
                count = 0
                indegree_count[x] -= 1
                if indegree_count[x] == 0:
                    deque.append(x)
                    count += 1

                if count > 1:
                    result = False
                    result_list = ["?"]
                    break
            if not result:
                break

        if len(result_list) != team_count:
            print("IMPOSSIBLE")
        else:
            print(" ".join(map(str, result_list)))
