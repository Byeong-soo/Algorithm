def solution(b):
    answer = -1

    for i in range(500000):
        j_squared = i ** 2 + b ** 2
        j = int(j_squared ** 0.5)
        if j ** 2 == j_squared and i + b > j:
            answer = j
            break

    return answer


if __name__ == '__main__':
    print(solution(5))
