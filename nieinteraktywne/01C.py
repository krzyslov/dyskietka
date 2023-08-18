# Program ilustrujący działanie neuronu o wielu wejściach
# i o charakterystyce liniowej.

# Przyjęto, że neuron ma 5 wejść, jednak można wybrać inną liczbę.

n = 5   # To jest wymiar wektora sygnałów wejściowych i wektora wag.
        # Zmiana tej wartości przeskaluje program dla innego typu neuronu.

sygnaly = [1,0,0,2,-1]
wagi = [1,-1,1,-1,1]

#podawanie wag
moc = 0
print("Neuron ma następujące wartości wag::")

for i in range(n):
    print(f"w({i+1})= {wagi[i]}")
    moc += wagi[i] * wagi[i]

print("\nMoc śladu pamięciowego =", moc)

    
#podawanie sygnałów

moc = 0
print("\nPrzystępujemy do eksperymentów.\n")
print("Składowe wektora wejściowego:")
for i in range(n):
    print(f"w({i}) = {wagi[i]}       x({i+1})= {sygnaly[i]}")
    moc += sygnaly[i] * sygnaly[i]

print("Moc sygnału wejściowego =", moc)


wyjscie = 0
for i in range(n):
    wyjscie += wagi[i] * sygnaly[i]
print("\n************ wyjście =", wyjscie)

