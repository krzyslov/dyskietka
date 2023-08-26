import math
import matplotlib.pyplot as plt

WAGI = [3,4]

# Wartości początkowe
n = 2
opis = ["pachnacy", "kolorowy"]

moc = 0


# Wprowadzanie wag
for i, (o,w) in enumerate(zip(opis,WAGI)):
    print(f"w({i+1}) czyli czy neuron lubi, gdy kwiat jest {o}: {w} ")


print("Polozenie obiektu wzorcowego:")


X1 = -2
X2 = -1
print(f"x(1) = {X1}")
print(f"x(2) = {X2}")

pobudzenie  = WAGI[0] * X1 + WAGI[1] * X2

plt.figure()
plt.title("Neuron Output")
plt.xlabel("X1")
plt.ylabel("X2")
plt.xlim(-10, 10)
plt.ylim(-10, 10)


plt.plot([0,WAGI[0]], [0,WAGI[1]], 'b--')
plt.plot([0, X1], [0, X2], 'r--')

plt.show()

print("    ***  wyjscie = ", pobudzenie)
