# Program ilustrujący działanie neuronu o wielu wejściach
# i o charakterystyce liniowej.

# Przyjęto, że neuron ma 5 wejść, jednak można wybrać inną liczbę.

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektora wag.
        # Zmiana tej wartości przeskaluje program dla innego typu neuronu.

sygnaly = [0] * n
wagi = [0] * n

while True:
    #podawanie wag
    while True:
        moc = 0
        print("Podaj współczynniki wag (dodatnie albo ujemne):")
        
        for i in range(n):
            wagi[i] = float(input(f"w({i+1})= "))

        print("\nDziękuję, neuron ma następujące wartości wag:")
        
        for i in range(n):
            print(f"w({i+1})= {wagi[i]}", end=" ")
            moc += wagi[i] * wagi[i]
        
        print("\nMoc śladu pamięciowego =", moc)

        decyzja = input("Czy chcesz zmienić (T/N): ")
        
        if decyzja.lower() == "n":
            break
        
    #podawanie sygnałów
    while True:
        moc = 0
        print("\nPrzystępujemy do eksperymentów.\n")
        print("Podaj składowe wektora wejściowego (dodatnie albo ujemne):")
        for i in range(n):
            sygnaly[i] = float(input(f"w({i}) = {wagi[i]}       x({i+1})= "))
            moc += sygnaly[i] * sygnaly[i]

        print("Moc sygnału wejściowego =", moc)
        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() == "n":
            break

    wyjscie = 0
    for i in range(n):
        wyjscie += wagi[i] * sygnaly[i]
    print("\n************ wyjście =", wyjscie)

    decyzja = input("\nSprawdzamy jeszcze jedną kombinację (T/N): ")
    if decyzja.lower() == "n":
        break
