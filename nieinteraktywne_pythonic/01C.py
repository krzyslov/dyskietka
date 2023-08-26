n = 5   # To jest wymiar wektora sygnałów wejściowych i wektora wag.
        # Zmiana tej wartości przeskaluje program dla innego typu neuronu.

SYGNALY = [1,0,0,2,-1]
WAGI = [1,-1,1,-1,1]

#podawanie wag
print("Neuron ma następujące wartości wag::")

for i,w in enumerate(WAGI):
    print(f"w({i+1})= {w}")

moc = sum(s ** 2 for s in WAGI)
print("\nMoc śladu pamięciowego =", moc)

    
#podawanie sygnałów

for i, (w,s) in enumerate(zip(WAGI,SYGNALY)):
    print(f"w({i}) = {w}       x({i+1})= {s}")

moc = sum(s ** 2 for s in SYGNALY)
print("Moc sygnału wejściowego =", moc)


wyjscie = sum(w * s for w, s in zip(WAGI, SYGNALY))
print("\n************ wyjście =", wyjscie)

