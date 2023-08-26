import numpy as np


SYGNALY =   [1,1,1,1,1]

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektorów wag.
        # Zmiana tej wartości przeskaluje program dla innego typu sieci.

m = 3   # To jest rozmiar sieci. Zmiana tej wartości pozwoli zbudować
        # inną sieć do innych zastosowań.

nazwy = [""] * n
wyjscie = [0] * m
wynik = [""] * m

# Dane wejściowe
nazwy = ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"]
wynik = ["ssak", "ptak", "ryba"]
wyjscie = [0] * m


wagi = [
    [4, 0.01, 0.01, -1, -1.5],
    [2, -1, 2, 2.5, 2],
    [-1, 3.5, 0.01, -2, 1.5]
]


# Wyświetlanie wag
for i, (wyn,wag) in enumerate(zip(wynik,wagi)):
    print(f"Dla neuronu o numerze {i+1} sygnalizującym przynależność do klasy '{wyn}':")
    for (naz,w) in zip(nazwy,wag):
        print(f"Dla wejścia o nazwie '{naz}', waga wynosi {w}")
    print()

# Pobranie wejść od użytkownika
print("Wpisane wejscia do sieci:")
for (naz,s) in zip(nazwy,SYGNALY):
    print(f"{naz} : {s}")

# Obliczanie wyników
print("******************** A oto wynik działania sieci. *********************")
print("Poniżej podane są sygnały wyjściowe dla wszystkich trzech neuronów sieci.\n")

wyjscie = 0
for j, (wyn,wag) in enumerate(zip(wynik,wagi)):
        wyjscie = sum(w*s for w,s in zip(wag,SYGNALY))
        print(f"************ neuron numer {j+1}, nazwa: {wyn} = {wyjscie}\n")


