def count(num, array):
    for i in range(len(array)):
        if int(array[i]) == num:
            return i


if __name__ == "__main__":
    num = input()
    _ = input()
    print count(num, raw_input().split(' '))
