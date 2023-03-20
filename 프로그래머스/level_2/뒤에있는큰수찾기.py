import collections


def solution(numbers):
    answer = []
    temp = []

    while numbers:
        pop = numbers.pop()
        temp_bool = False

        for i in range(len(temp)-1,-1,-1):
            if temp[i] > pop:
                answer.append(temp[i])
                temp_bool = True
                break
        if not temp_bool:
            answer.append(-1)
        temp.append(pop)
    answer.reverse()
    return answer


if __name__ == '__main__':
    print(solution([2, 3, 3, 5]))
