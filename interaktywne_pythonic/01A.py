n = 2  # Ten neuron ma tylko dwa wejścia, potem poznasz większe
SYGNALY = [0] * n
WAGI = [0] * n
opis = ["pachnący", "kolorowy"]


while True:
    while True:
        print("Podaj czy lubisz gdy kwiatek jest:")

        for i in range(n):
            WAGI[i] = float(input(f"{opis[i]}: "))

        print()
        moc = 0

        moc = sum(abs(w) for w in WAGI)

        print("Neuron ma następujące wartości wag:")

        for i in range(n):
            print(f"w({i}) = {WAGI[i]}")

        print()
        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() != "t":
            break

    while True:
        print("Podaj opis obiektu ocenianego. Czy ten kwiatek jest:")

        for i in range(n):
            SYGNALY[i] = float(input(f"{opis[i]}: "))

        print("Obiekt ma następujące wartości cech:")

        for i in range(n):
            print(f"x({i}) = {SYGNALY[i]}")

        print()

        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() != "t":
            break

    wyjscie = sum(WAGI[i] * SYGNALY[i] for i in range(len(WAGI)))

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
