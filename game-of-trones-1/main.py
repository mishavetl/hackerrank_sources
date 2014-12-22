"""
Game Of Thrones - 1 Hackerrank

author: mishavietl

"""

from collections import Counter

def count(string):

    count = Counter(string)
    rem_count = Counter((v % 2 for v in count.values()))

    if 1 in rem_count:
        return 'NO' if rem_count[1] > 1 else 'YES'

    else:
        return 'YES'


def main():
    for _ in range(input()):
        print count(raw_input())

main()
