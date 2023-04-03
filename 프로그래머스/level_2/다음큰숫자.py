# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    answer = 0

    one_count = bin(n).count("1")

    while True:
        n += 1
        if one_count == bin(n).count("1"):
            answer = n
            break
    return answer


if __name__ == '__main__':
    print(solution(78))
    print(solution(15))

