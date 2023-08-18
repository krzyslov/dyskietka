# Program ilustruje działanie jednowarstwowej sieci neuronowej.

# Przyjęto, że sieć zawiera 3 neurony, a każdy z nich ma 5 wejść.
# Sieć rozpoznaje zwierzęta (ssak, ryba, ptak) na podstawie 5 cech:
# ile ma nóg, czy żyje w wodzie, czy umie latać, czy jest pokryte piórami, czy rodzi się z jaj.

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektorów wag.
        # Zmiana tej wartości przeskaluje program dla innego typu sieci.

m = 3   # To jest rozmiar sieci. Zmiana tej wartości pozwoli zbudować
        # inną sieć do innych zastosowań.

sygnaly = [0] * n
nazwy = [""] * n
wyjscie = [0] * m
wynik = [""] * m
wagi = [[0] * n for _ in range(m)]

# Dane wejściowe
nazwy_data = ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"]
wynik_data = ["ssak", "ptak", "ryba"]

while True:
    wagi_data = [
        [4, 0.01, 0.01, -1, -1.5],
        [2, -1, 2, 2.5, 2],
        [-1, 3.5, 0.01, -2, 1.5]
    ]

    for i in range(n):
        nazwy[i] = nazwy_data[i]

    for i in range(m):
        wynik[i] = wynik_data[i]
        wagi[i] = wagi_data[i]

    # Wyświetlanie wag
    for i in range(m):
        print(f"Dla neuronu o numerze {i+1} sygnalizującym przynależność do klasy '{wynik[i]}':")
        for j in range(n):
            print(f"Dla wejścia o nazwie '{nazwy[j]}', waga wynosi {wagi[i][j]}")
        print()

    # Pobranie wejść od użytkownika
    sygnaly = [0] * n
    for i in range(n):
        sygnaly[i] = float(input(f"Podaj '{nazwy[i]}': "))

    # Obliczanie wyników
    print("******************** A oto wynik działania sieci. *********************")
    print("Poniżej podane są sygnały wyjściowe dla wszystkich trzech neuronów sieci.\n")

    for j in range(m):
        wyjscie[j] = sum(wagi[j][i] * sygnaly[i] for i in range(n))
        print(f"************ neuron numer {j+1}, nazwa: {wynik[j]} = {wyjscie[j]}\n")

    # Sprawdzanie kolejnej kombinacji
    decyzja = input("Sprawdzamy jeszcze jedną kombinację (T/N): ")
    if decyzja.lower() == "n":
        break

