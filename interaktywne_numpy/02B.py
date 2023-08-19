# Program ilustruje działanie sieci neuronowej z rywalizacją.
import numpy as np
n = 5
m = 3

SYGNALY = [0] * n
wyjscie = [0] * m
nazwy = ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"]
wynik = ["cos dziwnego ???", "ssak", "ptak", "ryba"]
wagi = [[4, 0.01, 0.01, -1, -1.5],
    [2, -1, 2, 2.5, 2],
    [-1, 3.5, 0.01, -2, 1.5]]


prog = 5

while True:
    
    print("Podaj składowe wektora wejściowego:")
    for i in range(n):
        SYGNALY[i] = float(input(f"{nazwy[i]} = "))
    
    print("\nPoszczególne neurony sieci mają następujące sygnały łącznego pobudzenia:\n")
    
    wyjscie[:m] = np.dot(wagi[:m], SYGNALY)

    print(*wyjscie[:m], sep=" ")
    
    numer = np.argmax(wyjscie[:m])
    if wyjscie[numer] <= prog:
        numer = 0
    else:
        numer += 1

    if numer == 0:
        print("Ponieważ żaden neuron nie wygrał, odpowiedź sieci brzmi:")
    else:
        print("\nW związku z wygraniem rywalizacji przez neuron", numer, "odpowiedź sieci brzmi:")

    print("************ To jest", wynik[numer], "\n")

    decyzja = input("Sprawdzamy jeszcze jedną kombinację (T/N): ")
    if decyzja.lower() != "t":
        break