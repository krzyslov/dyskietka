import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.layers import Dense
from sklearn import preprocessing

n = 2
SYGNALY = np.array([[-1, 2]])  # Nowe dane wejściowe z dwiema cechami
WAGI = np.array([1,2])
moc = np.sum(np.abs(WAGI))
# Normalizacja danych wejściowych
normalizer = preprocessing.Normalizer()
normalized_train_X = normalizer.fit_transform(SYGNALY)
Y_train = np.dot(WAGI,SYGNALY.T)

# Tworzenie modelu
model = Sequential()
model.add(Dense(units=1, input_dim=2, activation='linear', use_bias=False))

# Kompilacja modelu
model.compile(optimizer='sgd', loss='mean_squared_error')

# Trenowanie modelu
model.fit(normalized_train_X, Y_train, epochs=100)

# Przewidywanie na nowych danych

wyjscie = model.predict(normalized_train_X)  # Przewidywanie wyjścia

print()
print("************ Neuron obliczył swój sygnał wyjściowy, który wynosi:", wyjscie)
print("************ Oznacza to, że stosunek neuronu do tego kwiatka jest:")

if abs(wyjscie) < 0.2 * moc:
    print("obojetny")
elif wyjscie < 0:
    print("negatywny")
else:
    print("pozytywny")

print(f"Pożądany wynik: {Y_train}" )