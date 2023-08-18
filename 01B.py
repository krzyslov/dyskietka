import math
import matplotlib.pyplot as plt

# Wartości początkowe
n = 2
opis = ["pachnacy", "kolorowy"]
wagi = [0] * n
moc = 0

print("Nauron, ktory bedziesz badal bedzie dzielil obiekty,")
print("ktore mu za chwile")
print("pokazesz na takie, ktore lubi, oraz takie, ktorych nie lubi.")
print()
print("Teraz podasz wspolczynniki wag dla poszczegolnych cech obiektow.")
print("Wspolczynniki te moga byc dodatnie albo ujemne.")
print("Dodatnie wspolczynniki oznaczac beda aprobate dla danej cechy, a ujemne")
print("wskzaywac beda, ze dana cecha ma byc porzez neuron nie lubiana.")
print()
print("Teraz wazne juz beda tylko wartosci liczbowe wag i sygnalow wejsciowych.")
print("Jesli jednak chcesz, to mozesz dalej wyobrazac sobie, ze obiektami badanymi")
print("sa - jak w poprzednim programie - kwiaty. Podaj teraz, jakie maja byc wartosci")
print("wspolczynnikow wag (tzn. czy chcesz, by neuron lubil, gdy kwiat ma pewne cechy)")
print()

# Wprowadzanie wag
for i in range(n):
    opis_cechy = opis[i]
    wagi[i] = float(input(f"w({i+1}) czyli czy neuron lubi, gdy kwiat jest {opis_cechy}: "))
    moc += wagi[i] * wagi[i]

print("Polozenie obiektu wzorcowego")

while True:
    x1 = float(input("x(1) = "))
    x2 = float(input("x(2) = "))
    
    pobudzenie = 0
    for i in range(n):
        pobudzenie += wagi[i] * (x1 if i == 0 else x2)
    
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
