import sys

if __name__ == '__main__':
    store_list = list(sys.stdin.readline().rstrip())
    target = ""
    first_count = 0
    second_count = 0
    temp_num = 0
    temp_bool = False
    for i in range(len(store_list)):
        if store_list[i] != target:
            target = store_list[i]
            if temp_num > 0:
                first_count += temp_num - 1
            second_count += temp_num // 2
            temp_num = 1
            temp_bool = False
        elif store_list[i] == target:
            temp_num += 1
            temp_bool = True
    if temp_bool:
        first_count += temp_num - 1
        second_count += temp_num // 2

    print(str(first_count) + " " + str(second_count))
