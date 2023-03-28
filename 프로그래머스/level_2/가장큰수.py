# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    answer = ''

    string_numbers = []

    for num in numbers:
        string_numbers.append(str(num))

    string_numbers.sort(key=lambda num: num * 3, reverse=True)

    answer = str(int("".join(string_numbers)))


    return answer


if __name__ == '__main__':
    print(solution([6, 10, 2, 20]))
    print(solution([3, 30, 34, 5, 9]))
