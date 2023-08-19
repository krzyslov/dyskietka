# Program ilustruje działanie jednego neuronu
import numpy as np

n = 2  # Ten neuron ma tylko dwa wejścia, potem poznasz większe
sygnaly = [0] * n
wagi = [0] * n
opis = ["pachnący", "kolorowy"]


while True:
    while True:
        print("Podaj czy lubisz gdy kwiatek jest:")

        for i in range(n):
            wagi[i] = float(input(f"{opis[i]}: "))

        print()
        moc = 0

        moc = np.sum(np.abs(wagi))

        print("Neuron ma następujące wartości wag:")

        for i in range(n):
            print(f"w({i}) = {wagi[i]}")

        print()
        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() != "t":
            break

    while True:
        print("Podaj opis obiektu ocenianego. Czy ten kwiatek jest:")

        for i in range(n):
            sygnaly[i] = float(input(f"{opis[i]}: "))

        print("Obiekt ma następujące wartości cech:")

        for i in range(n):
            print(f"x({i}) = {sygnaly[i]}")

        print()

        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() != "t":
            break

    wyjscie = np.dot(wagi, sygnaly)

    print("\nNeuron obliczył swój sygnał wyjściowy, który wynosi:", wyjscie)
    print("Oznacza to, że stosunek neuronu do tego kwiatka jest:")

    if abs(wyjscie) < 0.2 * moc:
        print("obojetny")
    elif wyjscie < 0:
        print("negatywny")
    else:
        print("pozytywny")

    print()

    decyzja = input("Sprawdzamy jeszcze jedną kombinację (T/N): ")
    if decyzja.lower() == "n":
        break
