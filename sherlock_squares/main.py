"""
Sherlock And Squares Hackerrank

author: mishavietl

"""

from math import sqrt

def find_square_int(num1, num2):
    return int(sqrt(num2)) - int(sqrt(num1 - 1))

def main():
    for _ in range(input()):
        numbers = raw_input().split()
        print find_square_int(int(numbers[0]), int(numbers[1]))

main()
