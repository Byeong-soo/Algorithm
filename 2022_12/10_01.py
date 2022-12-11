import collections
import sys

# 9번 별찍기
# if __name__ == '__main__':
#     count = int(sys.stdin.readline().rstrip())
#
#     for i in range(1,count+1):
#         print("*" * i)

# 10번 기초 반복문 x 보다 작은 수
# if __name__ == '__main__':
#     list_count,target = map(int,sys.stdin.readline().rstrip().split(" "))
#     number_list = list(map(int,sys.stdin.readline().rstrip().split(" ")))
#
#     for i in number_list:
#         if i < target:
#             print(i,end=" ")

# 11 번 기초배열 최댓값
# if __name__ == '__main__':
#     index = 0
#     max_num = 0
#     max_count = 0
#
#     for i in range(9):
#         input_num = int(sys.stdin.readline().rstrip())
#         index += 1
#         if max_num < input_num:
#             max_num = input_num
#             max_count = index
#
#     print(max_num)
#     print(max_count)

# 12 기초 배열 OX 퀴즈
# if __name__ == '__main__':
#     test_count = int(sys.stdin.readline().rstrip())
#     for i in range(test_count):
#         total = 0
#         temp = 0
#         words = list(sys.stdin.readline().rstrip())
#         for j in words:
#             if j == "O":
#                 temp += 1
#                 total += temp
#             else:
#                 temp = 0
#         print(total)

# 13 기초배열 평균은 넘겠지
# if __name__ == '__main__':
# #     test_count = int(sys.stdin.readline().rstrip())
# #
# #     for i in range(test_count):
# #         points = list(map(int, input().split(" ")))
# #
# #         people = points[0]
# #         del points[0]
# #
# #         average = sum(points) / people
# #         newList = [x for x in points if x > average]
# #         answer = "%0.3f" % (round(len(newList) / people * 100, 3))
# #         print(f"{answer}%")

# 14 숫자
# if __name__ == '__main__':
#     total = [int(sys.stdin.readline().rstrip()) for x in range(3)]
#     mul = 1
#     for i in total:
#         mul *= i
#
#     num = [0 for x in range(10)]
#     for i in list(str(mul)):
#         num[int(i)] += 1
#
#     for i in num:
#         print(i)

# 15 기초 함수 정수 n개의 합

# 16 아스키 코드
# if __name__ == '__main__':
#     print(ord(sys.stdin.readline().rstrip()))

# 17 문자열 반복
# if __name__ == '__main__':
#     test_count = int(sys.stdin.readline().rstrip())
#
#     for i in range(test_count):
#         num, text = sys.stdin.readline().rstrip().split(" ")
#         text_list = list(text)
#         for x in text_list:
#             print(x * int(num),end="")
#         print()

# 18 단어의 개수
# if __name__ == '__main__':
#     text = (sys.stdin.readline().strip())
#     if len(text) == 0:
#         print(0)
#     else:
#         print(len(text.split()))



