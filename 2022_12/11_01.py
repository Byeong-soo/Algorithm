import sys


# 19 상수
# if __name__ == '__main__':
#     a, b = map(list,input().split(" "))
#
#     a = ''.join(a[::-1])
#     b = ''.join(b[::-1])
#
#     if int(a) > int(b):
#         print(a)
#     else:
#         print(b)

# 20 달팽이는 올라가고 싶다
# from math import ceil
#
# if __name__ == '__main__':
#     up, down, target = map(int, sys.stdin.readline().rstrip().split(" "))
#     one_day = up - down
#     temp = target - up
#
#     if target < up:
#         print(1)
#         exit()
#     else :
#         print(ceil(temp / one_day) + 1)

# 21 소수 찾기
# def check_prim_number(check_number):
#
#     for i in range(2,check_number):
#         if check_number % i == 0:
#             return False
#     return True
#
#
# if __name__ == '__main__':
#     answer = []
#     count = int(input())
#     numbers = list(map(int,input().split(" ")))
#
#     if 1 in numbers:
#         numbers.remove(1)
#
#     for number in numbers:
#         if check_prim_number(number):
#             answer.append(number)
#         numbers = [x for x in numbers if x % number != 0]
#
#     print(len(answer))

# 재귀함수
# def recursion(total,x):
#     total *= x
#     x -= 1
#
#     if x != 0:
#         recursion(total,x)
#     else:
#         print(total)
#         exit()
#
#
# if __name__ == '__main__':
#     sys.setrecursionlimit(10**7)
#     num = int(sys.stdin.readline().rstrip())
#     if num == 0:
#         print(1)
#     else:
#         recursion(1,num)

# 재귀함수가 뭔가요
# def what_is_recursion(index, target):
#     print("____" * index + "\"재귀함수가 뭔가요?\"")
#     print("____" * index + "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
#     print("____" * index + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
#     print("____" * index + "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
#
#     index += 1;
#     if index != target:
#         what_is_recursion(index, target)
#     else:
#         print("____" * index + "\"재귀함수가 뭔가요?\"")
#         print("____" * index + "\"재귀함수는 자기 자신을 호출하는 함수라네\"")
#
#     print("____" * index + "라고 답변하였지.")
#
#
# if __name__ == '__main__':
#     target = int(sys.stdin.readline().rstrip())
#     print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
#     what_is_recursion(0, target)
#     print("라고 답변하였지.")

# 카드놓기
