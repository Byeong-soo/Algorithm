# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        first = heapq.heappop(scoville)

        if first >= K:
            return answer

        if not scoville:
            return -1
        second = heapq.heappop(scoville)

        new_scovile = first + (second * 2)
        answer += 1
        heapq.heappush(scoville, new_scovile)

    return -1


if __name__ == '__main__':
    print(solution([1, 2, 3, 9, 10, 12], 7))
