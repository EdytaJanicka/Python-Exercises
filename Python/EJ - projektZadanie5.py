
def littleBorder(*args):

    amountOfSpaces = args[1]-2

    for i in range(args[0]):
        if i == 0 or i == args[0]-1:
            print(args[1]*'*')
        else:
            print('*'+amountOfSpaces*' '+'*')

try:
    print('Hej, chcesz zrobić ramkę z gwiazdek co? No to:')
    print('Podaj ilość wierszy')
    a = int(input())
    print('Podaj ilość kolumn')
    b = int(input())
    if a > 150 or b > 150:
        raise TypeError
    littleBorder(a, b)

except ValueError:
    print('Nie wpisuj znakow')
    quit()

except TypeError:
    print('Troche za duża ta ramka')
    quit()