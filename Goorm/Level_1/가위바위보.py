import sys

if __name__ == '__main__':
    kind_list = sys.stdin.readline().rstrip().split(" ")

    # num_set = set(kind_list)
    # kind_count = len(num_set)
    # if kind_count == 1 or kind_count == 3:
    #     print(0)
    # else:
    #     kind_first = num_set.pop()
    #     kind_second = num_set.pop()
    #
    #     if kind_first == "1" and kind_second == "2":
    #         print(kind_list.count(kind_second))
    #     elif kind_first == "2" and kind_second =="3":
    #         print(kind_list.count(kind_second))
    #     else:
    #         print(kind_list.count(kind_first))

    first = 0
    second = 0
    third = 0
    for i in kind_list:
        if i == "1":
            first += 1
        elif i == "2":
            second += 1
        else:
            third += 1
    if (first == 0 and second == 0) or (first == 0 and third == 0) or (second == 0 and third == 0) or (
            first != 0 and second != 0 and third != 0):
        print(0)
    elif first == 0:
        print(third)
    elif second == 0:
        print(first)
    elif third == 0:
        print(second)
