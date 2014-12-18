"""

The filling jars Hackerrank

author: mishavietl

"""

def count(a, b, k, answer):
    return answer + (b + 1 - a) * k

def main():
    n, m = raw_input().split()
    answer = 0

    for _ in range(int(m)):
        args = raw_input().split()
        answer = count(int(args[0]), int(args[1]), int(args[2]), answer)

    print answer / int(n)

main()
