"""

Alternating Characters Hackerrank

author: mishavietl

"""

def delete_copies(string):
    """deletes copies of letters"""
    amount_delete = 0

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            amount_delete += 1

    return amount_delete

def main():
    """main function"""
    for x in range(int(raw_input())):
        print delete_copies(raw_input())

main()
