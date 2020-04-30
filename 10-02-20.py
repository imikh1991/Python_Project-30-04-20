def counter(n):
    n = abs(n)

    result = 0

    while n != 0:
        result = result * 10 + n % 10
        n = n // 10
    print("ПЕРЕВЕРНУТОЕ ----> ")
    print(result)


if __name__ == '__main__':
    print("ВВЕДИТЕ ЧИСЛО ----> ")
    n = int(input())
    counter(n)
