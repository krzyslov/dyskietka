# Program ilustruje działanie sieci neuronowej z rywalizacją.

import numpy as np

SYGNALY =   [1,1,1,1,1]

n = 5
m = 3
wyjscie = [0] * m
# Dane wejściowe
nazwy = ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"]

wynik = ["cos dziwnego ???", "ssak", "ptak", "ryba"]

wagi = [
    [4, 0.01, 0.01, -1, -1.5],
    [2, -1, 2, 2.5, 2],
    [-1, 3.5, 0.01, -2, 1.5]
]

prog = 5

print("Podane składowe wektora wejściowego:")
for naz,syg in zip(nazwy,SYGNALY):
    print(f"{naz} = {syg}")

print("\nPoszczególne neurony sieci mają następujące sygnały łącznego pobudzenia:\n")

wyjscie = np.dot(wagi, SYGNALY)

print(*wyjscie, sep=" ")

print("\n")

if np.max(wyjscie) < prog:
     numer = 0
else:
     numer = np.argmax(wyjscie) + 1

if numer == 0:
    print("Ponieważ żaden neuron nie wygrał, odpowiedź sieci brzmi:")
    print("************ To jest", wynik[numer], "\n")
else:
    print("\nW związku z wygraniem rywalizacji przez neuron", numer, "odpowiedź sieci brzmi:")
    print("************ To jest", wynik[numer], "\n")
