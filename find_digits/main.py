"""

Find Digits Hackerrank

author: mishavietl

"""

def amount_of_divide_digits(number):
    """findes digits in number that divides on number"""
    number_s = str(number)
    amount = 0

    for d in number_s:
        d = int(d)
        if d != 0:
            if number % d == 0:
                amount += 1

    return amount

def input_u():
    """takes input from user"""
    amount_inputs = input()
    numbers = []
    for x in range(amount_inputs):
        numbers.append(input())
    return numbers

def main():
    """main function"""
    for num in input_u():
        print amount_of_divide_digits(num)


main()
