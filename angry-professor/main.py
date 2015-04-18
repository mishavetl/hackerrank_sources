#!/bin/python

def count(ar, n, k):
    answer = "YES"
    n_comed = 0
    for elem in ar:
        if n_comed == k:
            answer = "NO"
            break
        elif elem <= 0:
            n_comed += 1

    if n_comed == k:
        answer = "NO"

    print answer

if __name__ == "__main__":
    for _ in range(input()):
        n, k = [int(x) for x in raw_input().split()]
        ar = [int(i) for i in raw_input().split()]
        count(ar, n, k)
