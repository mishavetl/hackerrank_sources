"""

The manasa and stones Hackerrank

author: mishavietl

"""

def count(n, a, b):
    return sorted(set([i * a + (n - 1 - i) * b for i in range(n)]))

def main():
    for _ in range(input()):
        print ' '.join(map(str, count(input(), input(), input())))

main()
