# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()
    h_count = 0
    while citations:
        h_num = citations.pop()
        h_count += 1
        while citations[-1:] == h_num:
            citations.pop()
            h_count += 1
        if h_count >= h_num:
            return h_num

    return answer


if __name__ == '__main__':
    print(solution([3, 0, 6, 1, 5]))
    print(solution([1, 4, 5]))
    print(solution([5, 6, 7]))
