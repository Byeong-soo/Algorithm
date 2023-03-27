# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    clothe = {}

    for i in clothes:
        if i[1] not in clothe.keys():
            clothe[i[1]] = [i[0]]
        else:
            clothe[i[1]].append(i[0])

    for kind in clothe.keys():
        answer *= len(clothe[kind]) + 1

    return answer - 1


if __name__ == '__main__':
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))
