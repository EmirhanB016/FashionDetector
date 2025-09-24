from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Flask uygulamasını oluştur
app = Flask(__name__)

# Modeli yükle
model = load_model('kiyafet_modelim.h5')

# Kategori isimleri
etiket_adları = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# Ana sayfa rotası (buraya bir HTML dosyası döndüreceğiz)
@app.route("/")
def ana_sayfa():
    return render_template("index.html")

# Tahmin rotası (burada fotoğraf yüklenecek ve tahmin yapılacak)
@app.route("/tahmin", methods=['POST'])
def tahmin_yap():
    # Yüklenen dosyayı al
    foto = request.files['file']

    # Yüklenen dosyayı Pillow ile aç
    img = Image.open(foto)

    # Fotoğrafı önce RGB'ye sonra siyah-beyaza dönüştür
    img = img.convert('RGB').convert('L')

    # Fotoğrafı 28x28 piksel boyutuna getir
    img = img.resize((28, 28))

    # Numpy dizisine dönüştür ve 0-1 arasına ölçeklendir
    img_array = np.array(img) / 255.0

    # Piksel değerlerini tersine çevir (renkleri invert et)
    img_array = 1 - img_array

    # Modeli bir fotoğraf listesi beklediği için boyutu ayarla
    # (1, 784) şekline getirmek için
    img_array = img_array.reshape(1, 784)

    # Modeli kullanarak tahmin yap
    tahminler = model.predict(img_array)

    # En yüksek olasılığın indeksini bul
    tahmin_indeksi = np.argmax(tahminler[0])

    # İndekse karşılık gelen etiketi al
    tahmin_adi = etiket_adları[tahmin_indeksi]

    return f"{tahmin_adi}"

if __name__ == "__main__":
    app.run(debug=True)