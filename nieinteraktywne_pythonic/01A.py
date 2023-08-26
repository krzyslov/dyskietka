# Program ilustruje działanie jednego neuronu
n = 2  # Ten neuron ma tylko dwa wejścia, potem poznasz większe

WAGI = [1, 2]
SYGNALY = [-1,2]
opis = ["pachnący", "kolorowy"]



print("Neuron lubi, gdy kwiat jest:")
print(f"Pachnący: {WAGI[0]}")
print(f"Kolorowy: {WAGI[1]}\n")

moc = 0

moc = sum(abs(w) for w in WAGI)

print("Neuron ma następujące wartości wag:")

for i, w in enumerate(WAGI):
    print(f"w({i}) = {w}")

print("Obiekt ma następujące wartości cech:")

for o, s in zip(opis, SYGNALY):
    print(f"{o}: {s}")

print("Sygnały wejściowe wyglądają zatem następująco:")
for i, s in enumerate(SYGNALY):
    print(f"x({i}) = {s}")

print()


wyjscie = sum(w * s for w, s in zip(WAGI, SYGNALY))

print()
print("************ Neuron obliczył swój sygnał wyjściowy, który wynosi:", wyjscie)
print("************ Oznacza to, że stosunek neuronu do tego kwiatka jest:")

if abs(wyjscie) < 0.2 * moc:
    print("obojetny")
elif wyjscie < 0:
    print("negatywny")
else:
    print("pozytywny")