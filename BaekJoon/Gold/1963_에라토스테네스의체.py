import collections
import sys


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    # return [i for i in range(1000, n) if sieve[i] == True]
    return {str(i): False for i in range(1000, n) if sieve[i] == True}


if __name__ == '__main__':
    test_count = int(sys.stdin.readline().rstrip())

    for _ in range(test_count):
        prime = prime_list(9999)
        first_num, second_num = map(int, sys.stdin.readline().rstrip().split())

        deque = collections.deque([(first_num, 0)])
        result = "Impossible"
        while deque:
            pop_info = deque.popleft()

            pop = str(pop_info[0])
            count = pop_info[1]
            if pop == str(second_num):
                result = count
                break
            prime[pop] = True
            for i in range(10):
                for j in range(4):
                    temp = pop[:j] + str(i) + pop[j + 1:]

                    try:
                        if prime[temp] == False and int(temp) >= 1000:
                            prime[temp] = True
                            deque.append((temp, count + 1))
                    except KeyError:
                        continue

        print(result)
