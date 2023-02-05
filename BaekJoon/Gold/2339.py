import sys

if __name__ == '__main__':
    store_count = int(sys.stdin.readline().rstrip())
    store_list = list(map(int,sys.stdin.readline().rstrip().split(" ")))
    target = int(sys.stdin.readline().rstrip())

    distance = store_count//target
    result = []
    for i in range(0,store_count,distance):
        slice_store = store_list[i:i+distance]
        slice_store.sort()
        result.append(" ".join(map(str,slice_store)))

    print(" ".join(result))


