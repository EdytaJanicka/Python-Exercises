try:
    print('Podaj dzielną')
    a = int(input())
    print('Podaj dzielnik')
    b = int(input())

    if b > a:
        raise TypeError

    digits = str(a)
    t = 0
    res = 0
    addedValue = 0
    i = 0

    for d in digits:
        t = t * 10 + int(d)
        while t >= b:
            t -= b
            addedValue += 1
        res = res*10 + addedValue
        addedValue = 0

    while t != 0 and i <= 5:
        t *= 10
        while t >= b:
            t -= b
            addedValue += 1
        res += addedValue * 10**(-i-1)
        addedValue = 0
        i += 1

    print("Wynik dzielenia wynosi: ", "{:.5f}".format(res))

except ValueError:
    print('Nie wpisuj znakow')
    quit()

except TypeError:
    print('Nie możesz podać dzielnika większego niż dzielna')
    quit()