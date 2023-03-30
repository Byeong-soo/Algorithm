import time


# def solution(book_time):
#     answer = 0
#     room_list = []
#     book_time.sort(reverse=True)
#     print(book_time)
#     time_format = "%H:%M"
#
#     while book_time:
#         book = book_time.pop()
#         possible = False
#
#         for num in range(len(room_list)):
#             start_time = time.strptime(book[0], time_format)
#             end_time = time.strptime(room_list[num][1], time_format)
#
#             if start_time >= end_time + time.strptime("00:10", time_format):
#                 room_list[num] = book
#                 possible = True
#                 break
#         if not possible:
#             room_list.append(book)
#
#     answer = len(room_list)
#     return answer

def solution(book_time):
    answer = 0
    room_count = [0 for _ in range(6*24)]

    for book in book_time:
        split_start = book[0].split(":")
        split_end = book[1].split(":")

        start = int(split_start[0]) * 6 + (int(split_start[1]) // 10)
        end = int(split_end[0]) * 6 + (int(split_end[1]) // 10 + 1)

        for i in range(start,end):
            room_count[i] += 1

    answer = max(room_count)

    return answer

def time_convert(string) :
    h, m = map(int, string.split(":"))
    return h*60 + m


def solution(book_time):
    answer = 0
    check_change_list = list()
    for start, end in book_time :
        check_change_list.append((time_convert(start), 1))
        check_change_list.append((time_convert(end)+10, 0))

    check_change_list.sort()

    tmp = 0
    for t, chk in check_change_list :
        if chk == 0:
            tmp += -1
        else:
            tmp += 1
        answer = max(answer, tmp)
    return answer

if __name__ == '__main__':
    print(
        solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
    print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
    print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
