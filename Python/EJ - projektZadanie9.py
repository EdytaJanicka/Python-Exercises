import time
import datetime

def dateCounter(*args):
    
    a = args[0]
    b = args[1]
    c = args[2]
    d = datetime.datetime.now()
    dd = d.day
    md = d.month
    yd = d.year
    
    if b < md:
        s = yd - c
    else:
        s = yd - c - 1
    
    print("Od podanej daty upłynęło: ", s, " lat")
    print("Od podanej daty upłynęło: ", (12 - b + md + (yd - c) *12) - 12, " miesięcy")
    print("Od podanej daty upłynęło: ", (dd + md * 30 + (yd - c) * 365 + (12 - b) * 30 + 30 - a) - 390, " dni")

    return 0

try:
    print('Podaj dzien')
    a = int(input())
    print('Podaj miesiąc')
    b = int(input())
    print('Podaj rok')
    c = int(input())

    d = datetime.datetime.now()
    s = datetime.datetime(c, b, a)

    if a > 30 or b > 12 or a < 0 or b < 0 or c < 0:
        raise ValueError

    if d < s:
        raise TypeError

    dateCounter(a, b, c)

except ValueError:
    print('Nie wpisuj znakow/Nieprawidłowa data')
    quit()

except TypeError:
    print('Nie możesz podać daty wyższej niż dzisiaj???')
    quit()