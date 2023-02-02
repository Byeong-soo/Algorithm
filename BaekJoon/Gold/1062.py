import sys

if __name__ == '__main__':
    word_count, teach_word_count = map(int, sys.stdin.readline().rstrip().split(" "))
    # learn_word = [False for x in range(26)]
    basic_word = ["a", "n", "t", "i", "c"]

    # for word in basic_word:
    #     learn_word[ord(word) - 97] = True

    if teach_word_count <= 5:
        print(0)
        exit()

    teach_word_count -= 5

    for i in range(word_count):
        input_word = list(sys.stdin.readline().rstrip())
        word = input_word[4:-4]

