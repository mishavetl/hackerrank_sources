"""

The lovely letter mystery Hackerrank

author: mishavietl

"""

def count(money, price, discount):
    answer = money / price
    wrappers = answer

    while wrappers != 0:
        if wrappers >= discount:
            extra = wrappers / discount
            answer += extra
            wrappers = wrappers % discount + extra
        else:
            break

    return answer

def main():
    for i in range (int(raw_input())):
        money, price, discount = [int(x) for x in raw_input().split(' ')]

        print count(money, price, discount)

main()
