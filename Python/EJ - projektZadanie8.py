import random
import numpy as np
import matplotlib.pyplot as plt 
import collections

cipherArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
listOfNumbers = np.random.randint(1, 11, size=10000)
numbersCounter = collections.Counter(listOfNumbers)
countNumbers = [numbersCounter[i] for i in range(1, 11)]
chart = plt.bar(cipherArray, countNumbers, color="green", label='Ilość wystąpień')
plt.xlabel('Poszczególne wylosowane liczby')
plt.ylabel('Ilość wystąpien danej liczby')
plt.title("Ilość wystąpień liczb 1-10 w 10000 losowych liczbach")
plt.bar_label(chart, padding=2)
plt.legend()
plt.tight_layout()
plt.show()