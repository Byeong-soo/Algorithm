# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    answer = ''
    num_list = list(map(int, s.split(" ")))
    min_num = min(num_list)
    max_num = max(num_list)
    temp = [str(min_num),str(max_num)]
    answer = " ".join(temp)
    return answer


if __name__ == '__main__':
    print(solution("1 2 3 4"))
    print(solution("-1 -2 -3 -4"))
    print(solution("-1 -1"))
