import numpy as np

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektora wag.
        # Zmiana tej wartości przeskaluje program dla innego typu neuronu.

SYGNALY = [1,0,0,2,-1]
WAGI = [1,-1,1,-1,1]

#podawanie wag
print("Neuron ma następujące wartości wag::")

for i in range(n):
    print(f"w({i+1})= {WAGI[i]}")

moc = np.sum(np.square(WAGI))
print("\nMoc śladu pamięciowego =", moc)

    
#podawanie sygnałów

for i in range(n):
    print(f"w({i}) = {WAGI[i]}       x({i+1})= {SYGNALY[i]}")

moc = np.sum(np.square(SYGNALY))
print("Moc sygnału wejściowego =", moc)


wyjscie = np.dot(WAGI, SYGNALY)
print("\n************ wyjście =", wyjscie)

