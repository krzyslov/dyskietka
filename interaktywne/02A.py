import numpy as np

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektorów wag.
        # Zmiana tej wartości przeskaluje program dla innego typu sieci.

m = 3   # To jest rozmiar sieci. Zmiana tej wartości pozwoli zbudować
        # inną sieć do innych zastosowań.

SYGNALY = [0] * n

# Dane wejściowe
nazwy = ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"]
wynik = ["ssak", "ptak", "ryba"]
wyjscie = [0] * m

while True:
    wagi = [
        [4, 0.01, 0.01, -1, -1.5],
        [2, -1, 2, 2.5, 2],
        [-1, 3.5, 0.01, -2, 1.5]
    ]

    # Wyświetlanie wag
    for i in range(m):
        print(f"Dla neuronu o numerze {i+1} sygnalizującym przynależność do klasy '{wynik[i]}':")
        for j in range(n):
            print(f"Dla wejścia o nazwie '{nazwy[j]}', waga wynosi {wagi[i][j]}")
        print()

    # Pobranie wejść od użytkownika
    
    for i in range(n):
        SYGNALY[i] = float(input(f"Podaj '{nazwy[i]}': "))

    # Obliczanie wyników
    print("******************** A oto wynik działania sieci. *********************")
    print("Poniżej podane są sygnały wyjściowe dla wszystkich trzech neuronów sieci.\n")

    wyjscie[:m] = np.dot(wagi[:m], SYGNALY)


    for j in range(m):
        print(f"************ neuron numer {j+1}, nazwa: {wynik[j]} = {wyjscie[j]}\n")

    # Sprawdzanie kolejnej kombinacji
    decyzja = input("Sprawdzamy jeszcze jedną kombinację (T/N): ")
    if decyzja.lower() == "n":
        break

