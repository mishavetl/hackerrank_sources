"""

The lovely letter mystery Hackerrank

author: mishavietl

"""

def polindrom(string):
    """deletes copies of letters"""
    i_end = len(string) - 1
    amount = 0

    for i in range(len(string)):
        if ord(string[i_end]) < ord(string[i]):
            amount += ord(string[i]) - ord(string[i_end])

        elif ord(string[i_end]) > ord(string[i]):
            amount += ord(string[i_end]) - ord(string[i])

        if i_end == i or i_end - i == 1 or i_end - i == -1:
            break

        i_end -= 1

    return amount

def main():
    """main function"""
    for x in range(int(raw_input())):
        print polindrom(raw_input())

main()
