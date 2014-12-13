

def square_numbers(to_num):
    number = 1
    to_sum = 3
    numbers = []

    for x in range(to_num):
        numbers.append(number)
        number += to_sum
        to_sum += 2

    return numbers

print square_numbers(100000)
