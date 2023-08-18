# Program ilustruje działanie jednowarstwowej sieci neuronowej.

# Przyjęto, że sieć zawiera 3 neurony, a każdy z nich ma 5 wejść.
# Sieć rozpoznaje zwierzęta (ssak, ryba, ptak) na podstawie 5 cech:
# ile ma nóg, czy żyje w wodzie, czy umie latać, czy jest pokryte piórami, czy rodzi się z jaj.

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektorów wag.
        # Zmiana tej wartości przeskaluje program dla innego typu sieci.

m = 3   # To jest rozmiar sieci. Zmiana tej wartości pozwoli zbudować
        # inną sieć do innych zastosowań.

nazwy = [""] * n
wyjscie = [0] * m
wynik = [""] * m

# Dane wejściowe
nazwy_data = ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"]
sygnaly =   [0,1,1,-1,1]
wynik_data = ["ssak", "ptak", "ryba"]


wagi = [
    [4, 0.01, 0.01, -1, -1.5],
    [2, -1, 2, 2.5, 2],
    [-1, 3.5, 0.01, -2, 1.5]
]

for i in range(n):
    nazwy[i] = nazwy_data[i]

for i in range(m):
    wynik[i] = wynik_data[i]

# Wyświetlanie wag
for i in range(m):
    print(f"Dla neuronu o numerze {i+1} sygnalizującym przynależność do klasy '{wynik[i]}':")
    for j in range(n):
        print(f"Dla wejścia o nazwie '{nazwy[j]}', waga wynosi {wagi[i][j]}")
    print()

# Pobranie wejść od użytkownika
print("Wpisane wejscia do sieci:")
for i in range(n):
    print(f"{nazwy[i]} : {sygnaly[i]}")

# Obliczanie wyników
print("******************** A oto wynik działania sieci. *********************")
print("Poniżej podane są sygnały wyjściowe dla wszystkich trzech neuronów sieci.\n")

for j in range(m):
    wyjscie[j] = sum(wagi[j][i] * sygnaly[i] for i in range(n))
    print(f"************ neuron numer {j+1}, nazwa: {wynik[j]} = {wyjscie[j]}")


