def solution(number, limit, power):
    count_list = []

    for i in range(1, number + 1):
        count = 0
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                count += 2
            if j ** 2 == i:
                count -= 1

        if count > limit:
            count_list.append(power)
        else:
            count_list.append(count)

    answer = sum(count_list)
    return answer

if __name__ == '__main__':
    print(solution(5,3,2))
