def solution(answers):
    answer = []

    patterns = [[1, 2, 3, 4, 5],[2, 1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    pattern_count = [5,8,10]

    for pattern in range(3):
        answer_count = 0
        for i in range(len(answers)):
            answer_check = i % pattern_count[pattern]
            if answers[i] == patterns[pattern][answer_check]:
                answer_count += 1
        answer.append(answer_count)
    real_answer = []
    max_value = max(answer)
    if max_value == 0:
        return []
    else:
        for i in range(len(answer)):
            if max_value == answer[i]:
                real_answer.append(i+1)
    return real_answer


if __name__ == '__main__':
    print(solution([1,2,3,4,5]))
