# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):

    number_list_dic = dict.fromkeys(set(A), 0)

    for i in range(len(A)):
        number_list_dic[A[i]] += 1
    l = sorted(number_list_dic.items(), reverse=True)

    for i in range(len(l)):
        if l[i][0] == l[i][1]:
            return l[i][0]

    return 0

if __name__ == '__main__':
    print(solution([3, 8, 2, 3, 3, 2]))
