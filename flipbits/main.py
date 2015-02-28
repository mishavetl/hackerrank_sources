#!/usr/bin/python

def flipbits(num):
    nums = list(bin(num)[2:].zfill(32))
    num = ['1' if d == '0' else '0' for d in nums]

    return int(''.join(num), 2)

if __name__ == '__main__':
    for _ in range(int(raw_input())):
        print flipbits(int(raw_input()))
