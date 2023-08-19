import math
import matplotlib.pyplot as plt
import numpy as np

# Wartości początkowe
n = 2
opis = ["pachnacy", "kolorowy"]
wagi = [0] * n


# Wprowadzanie wag
for i in range(n):
    wagi[i] = float(input(f"w({i+1}) czyli czy neuron lubi, gdy kwiat jest {opis[i]}: "))


print("Polozenie obiektu wzorcowego")

while True:
    x1 = float(input("x(1) = "))
    x2 = float(input("x(2) = "))
    
    pobudzenie  = wagi[0] * x1 + wagi[1] * x2

    plt.figure()
    plt.title("Neuron Output")
    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    
    plt.plot([0,wagi[0]], [0,wagi[1]], 'b--')
    plt.plot([0, x1], [0, x2], 'r--')
    
    plt.show()
    
    print("    ***  wyjscie = ", pobudzenie)
    print(" - czy jeszcze jeden")
    decyzja = input("Czy kontynuować (T/N)? ").strip().lower()
    if decyzja != 't':
        break
