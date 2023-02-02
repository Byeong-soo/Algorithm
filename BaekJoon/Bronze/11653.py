import sys

if __name__ == '__main__':
    number = int(sys.stdin.readline().rstrip())

    for i in range(2, number + 1):
        while number % i == 0:
            print(i)
            number = number // i
        
