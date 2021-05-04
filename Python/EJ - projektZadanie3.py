import random

randomInt = (random.randint(1,100))
print('Hej, zgadnij jaką liczbe między 1 a 100 wymyśliłem!')

try:
    a = 0
    countTakes = 0

    while a!=randomInt:
        a = int(input())
        countTakes += 1
        if(a == randomInt):
            break
        
        if a > 100 or a < 0:
            print("Hej, ale liczba została wylosowana między 1 a 100, żeby Ci było łatwiej!")
        if a > randomInt :
            print('Liczba jest mniejsza niż', str(a))
        else:
            print('Liczba jest większa niż', str(a))
        print('Spróbuj jeszcze raz')
    
    print('Brawo liczba, o której myślałem to: ', str(randomInt)) 
    print('Zajęło Ci to ', str(countTakes), ' podejść')
except ValueError:
    print('Nie wpisuj znakow')
    quit()
