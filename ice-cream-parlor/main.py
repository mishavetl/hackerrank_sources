#!/bin/python

def count(ar, n, m):
    for i in range(m):
        counting = n - ar[i]
        if counting in ar:
            search = ar.index(counting)
            if search >= 0 and search != i:
                if search > i:
                    print str(i + 1) + " " + str(search + 1)
                else:
                    print str(search + 1) + " " + str(i + 1)

                break


if __name__ == "__main__":
    for _ in range(input()):
        n = input()
        m = input()
        ar = [int(i) for i in raw_input().split()]
        count(ar, n, m)
