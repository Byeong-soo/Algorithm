# def p(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return p(n-2) + p(n-1)
#

def fibonacci_numbers(num):
    first = 0
    second = 1
    tmep = 0

    while num - 1 != 0:
        temp = first
        first = second
        second = temp + second

        num -= 1
    return second


def solution(n):
    answer = 0
    answer = fibonacci_numbers(n) % 1234567

    return answer


if __name__ == '__main__':
    print(solution(3))
    print(solution(5))
