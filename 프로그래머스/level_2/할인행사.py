# https://school.programmers.co.kr/learn/courses/30/lessons/131127
import collections


def check(dic):
    for val in dic.values():
        if val > 0:
            return False
    return True


def solution(want, number, discount):
    answer = 0
    discount_count = {}
    for i in range(len(want)):
        discount_count[want[i]] = number[i]
    discount_list = collections.deque([])

    for i in range(len(discount) - 1, len(discount) - 11, -1):
        try:
            discount_list.append(discount[i])
            discount_count[discount[i]] -= 1
        except Exception:
            continue

    if check(discount_count):
        answer += 1

    rest_discount = discount[:-10]

    while rest_discount:
        try:
            out_item = discount_list.popleft()
            discount_count[out_item] += 1
        except Exception:
            pass

        try:
            in_item = rest_discount.pop()
            discount_list.append(in_item)
            discount_count[in_item] -= 1
        except Exception:
            pass

        if check(discount_count):
            answer += 1

    return answer


if __name__ == '__main__':
    print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
                   ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                    "banana", "apple", "banana"]))
    print(solution(["apple"], [10],
                   ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana",
                    "banana"]))
