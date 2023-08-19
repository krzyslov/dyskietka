# Program ilustrujący działanie neuronu o wielu wejściach
# i o charakterystyce liniowej.
import numpy as np

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektora wag.
        # Zmiana tej wartości przeskaluje program dla innego typu neuronu.

SYGNALY = [0] * n
WAGI = [0] * n

while True:
    #podawanie wag
    while True:
        moc = 0
        print("Podaj współczynniki wag (dodatnie albo ujemne):")
        
        for i in range(n):
            WAGI[i] = float(input(f"w({i+1})= "))

        print("\nDziękuję, neuron ma następujące wartości wag:")
        
        for i in range(n):
            print(f"w({i+1})= {WAGI[i]}", end=" ")
        
        moc = np.sum(np.square(WAGI))
        print("\nMoc śladu pamięciowego =", moc)

        decyzja = input("Czy chcesz zmienić (T/N): ")
        
        if decyzja.lower() == "n":
            break
        
    #podawanie sygnałów
    while True:
        print("\nPodaj składowe wektora wejściowego (dodatnie albo ujemne):")
        for i in range(n):
            SYGNALY[i] = float(input(f"w({i}) = {WAGI[i]}       x({i+1})= "))

        moc = np.sum(np.square(SYGNALY))
        print("Moc sygnału wejściowego =", moc)
        decyzja = input("Czy chcesz zmienić (T/N): ")
        if decyzja.lower() == "n":
            break

    wyjscie = np.dot(WAGI, SYGNALY)
    print("\n************ wyjście =", wyjscie)

    decyzja = input("\nSprawdzamy jeszcze jedną kombinację (T/N): ")
    if decyzja.lower() == "n":
        break
