def solution(babbling):
    possible = ["aya", "ye", "woo", "ma"]
    count = 0
    for word in babbling:
        for check in possible:
            if check in word:
                word = str(word).replace(check, " ", 1)
            if word.strip() == "":
                count += 1
                break
    return count


if __name__ == '__main__':
    print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
