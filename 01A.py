# Program ilustruje działanie jednego neuronu

n = 2  # Ten neuron ma tylko dwa wejścia, potem poznasz większe

sygnaly = [0] * (n + 1)
wagi = [0] * (n + 1)
opis = ["", "pachnący", "kolorowy"]

opis[1] = "pachnący"
opis[2] = "kolorowy"

while True:
    nowy = 1

    while True:
        print("Neuron, który będziesz badał, będzie dzielił obiekty, które mu za chwilę")
        print("pokarzesz, na takie, które lubi, oraz takie, których nie lubi.")
        print()
        print("Teraz podasz współczynniki wag neuronu dla poszczególnych cech obiektów.")
        print("Dodatnie współczynniki oznaczać będą aprobatę dla danej cechy, a ujemne")
        print("wskażą, że dana cecha ma być przez neuron nielubiana.")
        print()

        print("Załóżmy, że obiektami rozpoznawanymi są kwiaty. Podaj teraz, czy chcesz")
        print("by neuron lubił, gdy kwiat jest:")

        for i in range(1, n + 1):
            wagi[i] = float(input(f"{opis[i]}: "))

        print()
        moc = 0

        for i in range(1, n + 1):
            moc += abs(wagi[i])

        if nowy == 1:
            print("Dziękuję.")
        print("Neuron ma następujące wartości wag:")

        for i in range(1, n + 1):
            print(f"w({i}) = {wagi[i]}")

        print()
        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() != "t":
            break

    while True:
        if nowy == 1:
            print("Przystępujemy do eksperymentów.")
        print("Podaj opis obiektu ocenianego. Czy ten kwiatek jest:")

        for i in range(1, n + 1):
            sygnaly[i] = float(input(f"{opis[i]}: "))

        print("Dziękuję, obiekt ma następujące wartości cech:")

        for i in range(1, n + 1):
            print(f"x({i}) = {sygnaly[i]}")

        print()

        if nowy == 1:
            print("Porównaj składowe wektora wag neuronu i składowe wektora cech tego obiektu")
            print("Im bardziej będą one podobne do siebie, tym bardziej pozytywna będzie odpowiedź")

        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() != "t":
            break

    wyjscie = 0

    for i in range(1, n + 1):
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

    print()
    nowy = 0

    decyzja = input("Sprawdzamy jeszcze jedną kombinację (T/N): ")
    if decyzja.lower() == "t":
        nowy = 1
    else:
        break
