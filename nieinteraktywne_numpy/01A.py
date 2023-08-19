# Program ilustruje działanie jednego neuronu
import numpy as np
n = 2  # Ten neuron ma tylko dwa wejścia, potem poznasz większe

WAGI = [1, 2]
SYGNALY = [-1,2]
opis = ["pachnący", "kolorowy"]

print("Neuron lubi, gdy kwiat jest:")
print(f"Pachnący: {WAGI[0]}")
print(f"Kolorowy: {WAGI[1]}\n")

moc = 0

moc = np.sum(np.abs(WAGI))

print("Neuron ma następujące wartości wag:")

for i in range(0, n):
    print(f"w({i}) = {WAGI[i]}")

print("Obiekt ma następujące wartości cech:")

for i in range(0, n):
    print(f"{opis[i]}: {SYGNALY[i]}")

print("Sygnały wejściowe wyglądają zatem następująco:")
for i in range(0, n):
    print(f"x({i}) = {SYGNALY[i]}")

print()

wyjscie = np.dot(WAGI, SYGNALY)

print()
print("************ Neuron obliczył swój sygnał wyjściowy, który wynosi:", wyjscie)
print("************ Oznacza to, że stosunek neuronu do tego kwiatka jest:")

if abs(wyjscie) < 0.2 * moc:
    print("obojetny")
elif wyjscie < 0:
    print("negatywny")
else:
    print("pozytywny")