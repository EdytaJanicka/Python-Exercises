import random

try:
    randomNumbers = []
    i = 0
    while i < 6:
        rNumber = random.randint(1, 49)
        if randomNumbers.count(rNumber) == 0:
            randomNumbers.append(rNumber)
            i += 1
    
    print('Podaj 6 liczb z zakresu 1 - 49')
    userNumbers = []
    i = 0
    while i < 6:
        print('Podaj liczbę numer: ', str(i+1))
        uNumber = int(input())

        if 0 < uNumber <= 49 and uNumber not in userNumbers:
            userNumbers.append(uNumber)
            i += 1
    print('Wylosowane liczby to:', str(randomNumbers))
    print('Twoje liczby to:', str(userNumbers))
    checker = set(randomNumbers) & set(userNumbers)
    print ('Trafiony zatopiony! Liczba trafionych liczb: ', str(len(checker)))

except ValueError:
    print('Nie wpisuj znakow')
    quit()