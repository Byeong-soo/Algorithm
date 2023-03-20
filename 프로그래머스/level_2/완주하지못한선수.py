# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    while completion:
        completion_pop = completion.pop()
        participant_pop = participant.pop()

        if completion_pop != participant_pop:
            return participant_pop

    if len(participant) == 1:
        return participant.pop()
    return answer


if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
