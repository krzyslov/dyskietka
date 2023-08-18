import math
import matplotlib.pyplot as plt

# Wartości początkowe
n = 2
opis = ["pachnacy", "kolorowy"]
wagi = [3,4]
moc = 0

print("Nauron, ktory bedziesz badal bedzie dzielil obiekty,")
print("na takie, ktore lubi, oraz takie, ktorych nie lubi.")
print()
print("Wspolczynniki wag dla poszczegolnych cech obiektow moga byc dodatnie albo ujemne")
print("Dodatnie wspolczynniki oznaczaja aprobate dla danej cechy, a ujemne")
print("wskazuja, ze dana cecha ma byc poprzez neuron nie lubiana.")
print()
print("Wazne juz beda tylko wartosci liczbowe wag i sygnalow wejsciowych.")
print("Jesli jednak chcesz, to mozesz dalej wyobrazac sobie, ze obiektami badanymi")
print("sa - jak w poprzednim programie - kwiaty. Podaj teraz, jakie maja byc wartosci")
print("Podane zostały wartości wspolczynnikow wag")
print("tzn. mówią one, o tym czy kwiat lubi poszczególne cechy)")
print()

# Wprowadzanie wag
for i in range(n):
    print(f"w({i+1}) czyli czy neuron lubi, gdy kwiat jest {opis[i]}: {wagi[i]} ")
    moc += wagi[i] * wagi[i]

print("Polozenie obiektu wzorcowego:")


x1 = -2
x2 = -1
print(f"x(1) = {x1}")
print(f"x(2) = {x2}")

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
