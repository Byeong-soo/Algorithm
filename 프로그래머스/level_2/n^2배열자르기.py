# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []

    for num in range(left, right + 1):
        share = num // n
        extra = num % n

        start_num = share + 1

        if share >= extra:
            answer.append(start_num)
        elif share < extra:
            answer.append(start_num + extra - share)
    return answer


if __name__ == '__main__':
    print(solution(3, 2, 5))
    print(solution(4, 7, 14))
