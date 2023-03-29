# https://school.programmers.co.kr/learn/courses/30/lessons/17680
import collections


# 캐시 교체 알고리즘은 LRU(Least Recently Used)를 사용한다.
# cache hit일 경우 실행시간은 1이다.
# cache miss일 경우 실행시간은 5이다.

def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque([])

    for city in cities:
        temp = collections.deque([])
        find = False
        while cache:
            recent_city = cache.popleft()
            if recent_city == city.lower():
                temp.appendleft(recent_city)
                find = True
            else:
                temp.append(recent_city)
        cache = temp

        if find:
            answer += 1
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.appendleft(city.lower())
            else:
                cache.appendleft(city.lower())
                cache.pop()
    return answer


if __name__ == '__main__':
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
    print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
    print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                       "NewYork", "Rome"]))
    print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju",
                       "NewYork", "Rome"]))
    print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
    print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
