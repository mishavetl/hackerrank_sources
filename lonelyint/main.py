#!/usr/bin/python

def lonelyinteger(a):
    for n in a:
        i = [i for i, j in enumerate(a) if j == n]
        if len(i) < 2:
            return a[i[0]]

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
