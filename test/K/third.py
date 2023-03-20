# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    number_set = set(A)
    number_dic = dict.fromkeys(number_set, 0)
    sum_value = 0
    for i in range(len(A)):
        if number_dic[A[i]] < 2:
            number_dic[A[i]] += 1
    l = sorted(number_dic.items(), reverse=True)

    for i in range(1, len(l)):
        sum_value += l[i][1]
    return sum_value+1

if __name__ == '__main__':
    print(solution([1, 2]))
    print(solution([2, 5, 3, 2, 4, 1]))
    print(solution([2, 3, 3, 2, 2, 2, 1]))
