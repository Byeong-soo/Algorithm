# https://school.programmers.co.kr/learn/courses/30/lessons/12953
import math


def gcd(a, b):  # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)


def solution(arr):
    answer = 1
    while arr:
        pop = arr.pop()
        answer = int(lcm(answer,pop))

    return answer


if __name__ == '__main__':
    print(solution([2,6,8,14]))
    print(solution([1,2,3]))
