def solution(n):
    answer = 0
    now = 1
    now_sum = 0
    pre_sum = 1
    m_pre_sum = 0

    while now != n:
        now_sum = pre_sum + m_pre_sum
        m_pre_sum = pre_sum
        pre_sum = now_sum
        now+=1

    answer = pre_sum

    return answer % 1234567


if __name__ == '__main__':
    print(solution(5))
