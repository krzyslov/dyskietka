# Program ilustruje działanie jednego neuronu

n = 2  # Ten neuron ma tylko dwa wejścia, potem poznasz większe

wagi = [1, 2]
sygnaly = [-1,2]
opis = ["pachnący", "kolorowy"]

print("Neuron, dzieli obiekty na takie, które lubi oraz takie, które nie lubi")
print("Przypisane zostały współczynniki wag neuronu dla poszczególnych cech obiektów.")
print("Dodatnie współczynniki oznaczają probatę dla danej cechy, a ujemne")
print("wskazuje, że dana cecha ma być przez neuron nielubiana.")
print()

print("Załóżmy, że obiektami rozpoznawanymi są kwiaty")
print("Neuron lubi, gdy kwiat jest:")
print(f"Pachnący: {wagi[0]}")
print(f"Kolorowy: {wagi[1]}\n")

moc = 0

for i in range(0, n ):
    moc += abs(wagi[i])

print("Neuron ma następujące wartości wag:")

for i in range(0, n):
    print(f"w({i}) = {wagi[i]}")

print("\nPrzystępujemy do eksperymentów.")
print("Obiekt ma następujące wartości cech:")

for i in range(0, n):
    print(f"{opis[i]}: {sygnaly[i]}")

print("Sygnały wejściowe wyglądają zatem następująco:")
for i in range(0, n):
    print(f"x({i}) = {sygnaly[i]}")

print()

print("Porównaj składowe wektora wag neuronu i składowe wektora cech tego obiektu")
print("Im bardziej będą one podobne do siebie, tym bardziej pozytywna będzie odpowiedź")


wyjscie = 0

for i in range(0, n):
    wyjscie += wagi[i] * sygnaly[i]

print()
print("************ Neuron obliczył swój sygnał wyjściowy, który wynosi:", wyjscie)
print("************ Oznacza to, że stosunek neuronu do tego kwiatka jest:")

if abs(wyjscie) < 0.2 * moc:
    print("obojetny")
elif wyjscie < 0:
    print("negatywny")
else:
    print("pozytywny")