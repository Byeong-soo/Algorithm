import heapq
import sys

if __name__ == '__main__':
    point_count, line_count = map(int, sys.stdin.readline().rstrip().split(" "))
    start_point = int(sys.stdin.readline().rstrip())
    point_map = [[] for _ in range(point_count + 1)]
    min_price = [float("inf") for _ in range(point_count + 1)]
    visited = [False for _ in range(point_count + 1)]

    for i in range(line_count):
        start, end, price = map(int, sys.stdin.readline().rstrip().split(" "))
        point_map[start].append([price, end])

    heapq_city = []
    heapq.heappush(heapq_city, (0, start_point))
    min_price[start_point] = 0
    visited[start_point] = True
    while heapq_city:
        pop_city = heapq.heappop(heapq_city)

        for city_info in point_map[pop_city[1]]:
            city_number = city_info[1]
            city_price = city_info[0]
            min_price[city_number] = min(city_price + min_price[pop_city[1]], min_price[city_number])
            if not visited[city_number]:
                heapq.heappush(heapq_city, (min_price[city_number], city_number))
                visited[city_number] = True

    for i in range(1, point_count + 1):
        if min_price[i] != float("inf"):
            print(min_price[i])
        else:
            print("INF")
