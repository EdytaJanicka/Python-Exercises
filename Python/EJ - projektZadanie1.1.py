
try:
    print('Podaj pierwsza liczbe')
    a = int(input())
    print('Podaj druga liczbe')
    b = int(input())
    x = 0
    c = a
    d = b
    if a > b: 
        for i in range(b,a+1):
            x = x + b
            b = b + 1
    elif b > a:
        for i in range(a,b+1):
            x = x + a
            a = a + 1
    print('Suma liczb calkowitych pomiedzy '+str(c)+', a '+str(d)+' wynosi :')
    print(str(x))

except ValueError:
    print('Nie wpisuj znakow')
    quit()
