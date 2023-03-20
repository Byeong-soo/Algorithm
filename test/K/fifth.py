# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, N):
    need_count = 0
    max_size = 0
    temp = 0
    if N != 0:
        temp = int(N ** 0.5) + 1
        need_count = ((temp ** 2) - N) * 4
        if need_count <= M:
            M -= need_count
            max_size = temp * 2
        else:
            max_size = (temp - 1) * 2
    while M > 0:
        need_count = (max_size * 2) + 1

        if M < need_count:
            break
        else:
            M -= need_count
            max_size += 1
    return max_size


if __name__ == '__main__':
    print(solution(8, 0))
    print(solution(4, 3))
    print(solution(0, 18))
    print(solution(13, 3))
