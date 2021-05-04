
file = open("projektowe.txt", "r")
stringFromFile = file.read()
chars = {}

for char in stringFromFile:
    if char in chars:
        chars[char] = chars[char] + 1
    else:
        chars[char] = 1
file.close()
print("Plik zawiera nastepujace znaki w takiej ilosci: ")
print(chars)
print("Ilość znaków w pliku projektowe.txt: ", len(stringFromFile))