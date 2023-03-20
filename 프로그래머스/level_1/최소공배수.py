def solution(numer1, denom1, numer2, denom2):
    answer = []
    lcm = 0
    gcd = 0
    for i in range(max(denom1, denom2), denom1 * denom2 + 1):
        if i % denom1 == 0 and i % denom2 == 0:
            lcm = i
            break
    sum_number = (numer1 * (lcm // denom1)) + (numer2 * (lcm // denom2))

    for i in range(min(sum_number, lcm), 0, -1):
        if sum_number % i == 0 and lcm % i == 0:
            gcd = i
            break

    answer = [sum_number // gcd, lcm // gcd]
    return answer
