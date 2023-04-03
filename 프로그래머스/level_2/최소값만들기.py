# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A, B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    while A:
        a_pop = A.pop()
        b_pop = B.pop()
        answer += a_pop * b_pop

    return answer


if __name__ == '__main__':
    print(solution([1, 4, 2], [5, 4, 4]))
    print(solution([1, 2], [3, 4]))
