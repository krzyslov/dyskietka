import math
import matplotlib.pyplot as plt
import numpy as np

# Wartości początkowe
n = 2
opis = ["pachnacy", "kolorowy"]
WAGI = [0] * n
X1 = 0
X2 = 0

# Wprowadzanie wag
for i in range(n):
    WAGI[i] = float(input(f"w({i+1}) czyli czy neuron lubi, gdy kwiat jest {opis[i]}: "))


print("Polozenie obiektu wzorcowego")

while True:
    X1 = float(input("x(1) = "))
    X2 = float(input("x(2) = "))
    
    pobudzenie  = WAGI[0] * X1 + WAGI[1] * X2

    plt.figure()
    plt.title("Neuron Output")
    plt.xlabel("X1")
    plt.ylabel("X2")
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    
    plt.plot([0,WAGI[0]], [0,WAGI[1]], 'b--')
    plt.plot([0, X1], [0, X2], 'r--')
    
    plt.show()
    
    print("    ***  wyjscie = ", pobudzenie)
    print(" - czy jeszcze jeden")
    decyzja = input("Czy kontynuować (T/N)? ").strip().lower()
    if decyzja != 't':
        break
