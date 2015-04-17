def count(num):
    if num < 3:
        return -1
    elif num == 5:
        return 33333
    elif num == 3:
        return 555
    elif num % 3 == 0:
        return int('555' * (num / 3))
    else:
        answer = ''
        for _ in range(num):
            if num == 10:
                return int(answer + ('33333' * 2))

            elif num == 5:
                return int(answer + '33333')

            if num < 5:
                return -1

            answer += '555'
            num -= 3



if __name__ == "__main__":
    for _ in range(input()):
        print count(input())
