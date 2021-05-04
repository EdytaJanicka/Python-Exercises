try:
    print('Podaj co najmniej 8-literowe slowo')
    slowo = str(input())
    
    a = len(slowo)
    b = slowo.isalpha()

    if a < 8: raise ValueError
    if b == False: raise ValueError

    slowo1 = slowo[:3]
    slowo2 = slowo[-2]
    slowo3 = slowo[-4:]
    slowo4 = slowo[1:-1]
    slowo5 = slowo4[::-1]

    
    print('3 pierwsze znaki : '+slowo1)
    print('2 znak od konca : '+slowo2)
    print('ostatnie 4 znaki : '+slowo3)
    print('znaki od 2 do przedostatniego - odwrócone : '+slowo5)



except ValueError:
    print('Slowo jest za krotkie lub nie sklada sie z samych znakow')
    quit()