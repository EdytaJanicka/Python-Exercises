
def lookForNumber(*args):
    
    a = args[0]
    b = args[1]
    c = args[2]
    
    if c == 1:
        return a
    else:
        return b + lookForNumber(a, b, c - 1) 

try:
    print('Podaj wyraz początkowy')
    a = int(input())
    print('Podaj różnicę ciągu')
    b = int(input())
    print('Podaj który wyraz ciągu chciałbyś wyświetlić')
    c = int(input())

    if c <= 0:
        raise TypeError

    print(lookForNumber(a, b, c))

except ValueError:
    print('Nie wpisuj znakow')
    quit()

except TypeError:
    print('Nie możesz podać ujemnego wyrazu ciągu???')
    quit()