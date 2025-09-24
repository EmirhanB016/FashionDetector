import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 1. Veriyi yükleme ve ön işleme
(egitim_resimleri, egitim_etiketleri), (test_resimleri, test_etiketleri) = tf.keras.datasets.fashion_mnist.load_data()

egitim_resimleri = egitim_resimleri / 255.0
test_resimleri = test_resimleri / 255.0

egitim_resimleri = egitim_resimleri.reshape(60000, 784)
test_resimleri = test_resimleri.reshape(10000, 784)

# 2. Modeli oluşturma ve derleme
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 3. Modeli eğitme
model.fit(egitim_resimleri, egitim_etiketleri, epochs=10)

# 4. Modelin performansını değerlendirme
test_kayıp, test_doğruluk = model.evaluate(test_resimleri, test_etiketleri)
print('\nTest doğruluğu:', test_doğruluk)

model.save('kiyafet_modelim.h5')

# 5. Tek bir fotoğraf üzerinde tahmin yapma
tahminler = model.predict(test_resimleri)

# Etiket adları
etiket_adları = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# İlk test fotoğrafının tahminini bulma
tahmin_indeksi = np.argmax(tahminler[0])
tahmin_adi = etiket_adları[tahmin_indeksi]
gercek_etiket = etiket_adları[test_etiketleri[0]]

print(f"\nModelin tahmini: {tahmin_adi}")
print(f"Gerçek etiket: {gercek_etiket}")