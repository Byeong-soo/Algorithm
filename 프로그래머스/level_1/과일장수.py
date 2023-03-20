def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0

    for i in range(m-1,len(score),m):
        answer += score[i] * m
    return answer


if __name__ == '__main__':
    print(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))
