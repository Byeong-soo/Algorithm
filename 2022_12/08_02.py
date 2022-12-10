import sys

# 1번 hello world 출력하기
# if __name__ == '__main__':
#     print("Hello World!")

# 2번 사칙연산 입출력
# if __name__ == '__main__':
#     first, second = map(int, sys.stdin.readline().rstrip().split(" "))
#     print(first + second)
#     print(first - second)
#     print(first * second)
#     print(first // second)
#     print(first % second)

# 3번 곱셈
# if __name__ == '__main__':
#     first = int(sys.stdin.readline().rstrip())
#     second = int(sys.stdin.readline().rstrip())
#     temp1 = second
#     temp = 0
#
#     temp = second % 10
#     print(first * temp)
#     temp1 -= temp
#
#     temp = temp1 % 100
#     print(first * (temp) // 10)
#     temp1 -= temp
#
#     temp = temp1 % 1000
#     print((first * temp) // 100)
#
#     print(first*second)
# 과거의 풀이... 좀더 잘풀었네...
#
#     a = input()
#     b = input()
#
#     a = int(a)
#     b = int(b)
#
#     c = a*b
#     for i in range(0, 3):
#         print(a * (b % 10))
#         b = int(b/10)
#
#     print(c)

# 4번 시험 성적
# if __name__ == '__main__':
#  point = int(sys.stdin.readline().rstrip())
#
#  if point >= 90:
#      print("A")
#  elif point >= 80:
#      print("B")
#  elif point >= 70:
#      print("C")
#  elif point >= 60:
#      print("D")
#  else :
#      print("F")

# 5번 윤년
# if __name__ == '__main__':
#     year = int(sys.stdin.readline().rstrip())
#
#     if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
#         print(1)
#     else:
#         print(0)

# 6번 직사각형에서 탈출
# if __name__ == '__main__':
#     x, y, w, h = map(int, sys.stdin.readline().rstrip().split(" "))
#     print(min(x, y, w - x, h - y))

# 7번 구구단
# if __name__ == '__main__':
#     x = int(sys.stdin.readline().rstrip())
#
#     for i in range(1, 10):
#         print(str(x) + " * " + str(i) + " = " + str(x * i))

# 8번 반복문
if __name__ == '__main__':
    test_count = int(sys.stdin.readline().rstrip())

    for i in range(test_count):
        first, second = map(int,(sys.stdin.readline().rstrip().split(" ")))
        print((first + second))