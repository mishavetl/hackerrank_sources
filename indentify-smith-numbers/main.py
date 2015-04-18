#!/bin/python

def count(n):
    answer = 0
    sum_p = 0
    sum_d = 0
    i = 2

    for d in list(str(n)):
        sum_d += int(d)

    while n > 0 and i <= n:
        while n % i == 0:
            for d in list(str(i)):
                sum_p += int(d)
            n = n / i
        i = i + 1

    if sum_p == sum_d:
        answer = 1

    print answer

if __name__ == "__main__":
    count(input())
