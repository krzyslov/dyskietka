# Program ilustruje działanie sieci neuronowej z rywalizacją.

n = 5
m = 3

sygnaly = [0] * (n + 1)
nazwy = [""] * (n + 1)
wyjscie = [0] * (m + 1)
wynik = [""] * (m + 1)
wagi = [[0] * (n + 1) for _ in range(m + 1)]

dane = [
    ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"],
    ["ssak", "ptak", "ryba"],
    [4, 0.01, 0.01, -1, -1.5],
    [2, -1, 2, 2.5, 2],
    [-1, 3.5, 0.01, -2, 1.5]
]

for i in range(1, n + 1):
    nazwy[i] = dane[0][i - 1]

for i in range(1, m + 1):
    wynik[i] = dane[1][i - 1]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        wagi[i][j] = dane[i + 1][j - 1]

prog = 5
wynik[0] = "cos dziwnego ???"

print("Sieć jest już nauczona, dokładnie tak samo jak poprzednia (z programu 02A.BAS)")
print("Dlatego od razu przystępujemy do eksperymentów.\n")

while True:
    sygnaly = [0] * (n + 1)
    
    print("Podaj składowe wektora wejściowego:")
    for i in range(1, n + 1):
        nazwa = nazwy[i]
        sygnaly[i] = float(input(f"{nazwa} = "))
    
    print("\nPoszczególne neurony sieci mają następujące sygnały łącznego pobudzenia:\n")
    
    for j in range(1, m + 1):
        wyjscie[j] = 0
        
        for i in range(1, n + 1):
            wyjscie[j] += wagi[j][i] * sygnaly[i]
        
        print(wyjscie[j], end=" ")
    
    print("\n")
    
    numer = 0
    wartosc = prog
    
    for j in range(1, m + 1):
        if wyjscie[j] > wartosc:
            numer = j
            wartosc = wyjscie[j]
    
    if numer == 0:
        print("Ponieważ żaden neuron nie wygrał, odpowiedź sieci brzmi:")
        print("************ To jest", wynik[numer], "\n")
        decyzja = input("Sprawdzamy jeszcze jedną kombinację (T/N): ")
        if decyzja.lower() != "t":
            break
    else:
        print("\nW związku z wygraniem rywalizacji przez neuron", numer, "odpowiedź sieci brzmi:")
        print("************ To jest", wynik[numer], "\n")
        decyzja = input("Sprawdzamy jeszcze jedną kombinację (T/N): ")
        if decyzja.lower() != "t":
            break
