"""

The halloween party Hackerrank

author: mishavietl

"""

def count(cuts):
    return (cuts / 2) * (cuts - cuts / 2)

def main():
    for _ in range(input()):
        print count(input())

main()
