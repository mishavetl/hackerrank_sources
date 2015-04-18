#!/bin/python

def cut_sticks(ar, m):
    ar.sort()
    complete = False
    while not complete:
        x = 0
        if m != 0:
            print m
            for _ in range(ar.count(ar[0])):
                del ar[0]
                m -= 1
        else:
            complete = True



if __name__ == "__main__":
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    cut_sticks(ar, m)
