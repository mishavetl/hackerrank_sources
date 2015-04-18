#!/bin/python
def insertionSort(ar, m):
    for i in range(1, m):
        on_deck = ar[i]
        compare = i - 1

        while compare >= 0 and on_deck < ar[compare]:
            ar[compare+1] = ar[compare]
            ar[compare] = on_deck
            compare -= 1

        if i != m - 1:
            print ' '.join([str(num) for num in ar])


    print ' '.join([str(num) for num in ar])

if __name__ == "__main__":
    m = input()
    ar = [int(i) for i in raw_input().strip().split()]
    insertionSort(ar, m)
