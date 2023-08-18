# Program ilustruje działanie sieci neuronowej z rywalizacją.

n = 5
m = 3



# Dane wejściowe
nazwy = ["ilosc nog", "zyje w wodzie", "umie latac", "ma piora", "jajorodne"]
sygnaly =   [4,-1,-1,-1,-1]
wynik = ["cos dziwnego ???", "ssak", "ptak", "ryba"]
wyjscie = [0] * m

wagi = [
    [4, 0.01, 0.01, -1, -1.5],
    [2, -1, 2, 2.5, 2],
    [-1, 3.5, 0.01, -2, 1.5]
]

prog = 5

print("Sieć jest już nauczona, dokładnie tak samo jak poprzednia (z programu 02A.BAS)")
print("Dlatego od razu przystępujemy do eksperymentów.\n")


print("Podane składowe wektora wejściowego:")
for i in range(n):
    print(f"{nazwy[i]} = {sygnaly[i]}")

print("\nPoszczególne neurony sieci mają następujące sygnały łącznego pobudzenia:\n")

for j in range(m):
    wyjscie[j] = 0
    
    for i in range(n):
        wyjscie[j] += wagi[j][i] * sygnaly[i]
    
    print(wyjscie[j], end=" ")

print("\n")

numer = 0
wartosc = prog

for j in range(1,m+1):
    if wyjscie[j-1] > wartosc:
        numer = j
        wartosc = wyjscie[j-1]

if numer == 0:
    print("Ponieważ żaden neuron nie wygrał, odpowiedź sieci brzmi:")
    print("************ To jest", wynik[numer], "\n")
else:
    print("\nW związku z wygraniem rywalizacji przez neuron", numer, "odpowiedź sieci brzmi:")
    print("************ To jest", wynik[numer], "\n")
