# 👕 FashionDetector: Kıyafet Tespit Uygulaması
> NOT: Bu projede "Fashion-MNIST" veri seti kullanılmış ve proje yapay zeka yardımıyla yapılmıştır!!!

---

## 💡 Proje Hakkında
Bu proje, **derin öğrenme (Deep Learning)** tekniklerini kullanarak yüklediğiniz kıyafet fotoğraflarının "**Tişört**", "**Elbise**", "**Spor Ayakkabı**", "**Çanta**" gibi kategorilerinden hangisine ait olduğunu belirleyen bir **web uygulamasıdır**. `FashionDetector` adını taşıyan bu uygulama, kullanıcıların yüklediği kıyafet fotoğraflarının hangi kategoriye ait olduğunu yapay zeka yardımıyla tahmin etmeyi amaçlar.

### 🌟 Temel Hedef:
* Kullanıcıların kıyafetlerin ne olduğunu kolayca tahmin etmesini sağlamak.
---

## ✨ Özellikler

* **Gerçek Zamanlı Tahmin:** Kullanıcıların yüklediği kıyafet fotoğrafına göre model, resmi **AJAX** kullanarak tahminin sayfa yenilenmeden anında gösterilmesini sağlar.
* **Kullanıcı Dostu Web Arayüzü:** HTML sayfası üzerinden fotoğraf yükleme, ve “Tahmin Et” butonu ile kolay bir kullanım sunar.
* **API Entegrasyonu:** `/tahmin` uç noktası üzerinden dosya kabul edilir, yapay zeka modeliyle tahmin yapar ve sonuç olarak tahmin edilen kıyafetin adını döndürür.
---

## 🚀 Hızlı Başlangıç & Demo

Uygulamanın nasıl çalıştığını merak mı ediyorsunuz? İşte hızlı bir bakış ve demolar:

1.  **Uygulamayı Başlatın:** "Kurulum ve Çalıştırma" bölümündeki adımları takip ederek `app.py` dosyasını çalıştırın.
2.  **Web Arayüzünü Açın:** Terminaldeki "Running on http://..." linkine tıklayın.
3.  **Fotoğraf Yükleyin:** Arayüze bir kıyafet fotoğrafı yükleyin ve tahmin sonucunu anında görün!

| Uygulama Arayüzü                       | Tahmin Sonucu Demousu                       |
| :------------------------------------- | :------------------------------------------ |
| ![Uygulama Arayüzü](images/uygulama_arayuzu.png) | ![Tahmin Demousu](images/uygulama_demo.gif) |

---

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler

Bu proje geliştirilirken aşağıdaki teknolojiler ve Python kütüphaneleri kullanılmıştır:

* **Python:** Projenin ana programlama dili olarak kullanılmıştır.
* **Flask:** Basit bir web sunucusu ve API oluşturmak için kullanılmıştır.
* **TensorFlow / Keras:** Önceden eğitilmiş `.h5` formatındaki derin öğrenme modelinin yüklenmesi ve tahmin işlemleri için kullanılır.
* **Pillow:** Kullanıcıdan gelen fotoğraf verisini okumak, uygun boyutlandırma ve ön işleme adımlarını gerçekleştirmek için kullanılır.
* **NumPy:** Görüntü verilerini sayısal dizilere dönüştürmek ve bu diziler üzerinde gerekli matematiksel işlemleri yapmak için kullanılır.

### 📊 Veri Kaynakları

* Projede kullanılan kıyafet fotoğraflarının her biri "Fashion-MNIST" datasetinten alınmıştır.

---

## ⚙️ Kurulum ve Çalıştırma

Projenizi yerel ortamınızda çalışır hale getirmek için aşağıdaki adımları takip edebilirsiniz:

1.  **Projeyi Klonlama:** Projeyi GitHub'dan indirin veya klonlayın.   
2.  **Python Sürümü Kontrolü:** Sisteminizde **Python 3.8-3.10** yüklü olduğundan emin olun. 
3.  **Bağımlılıkları Yükleme:** Projenin tüm Python kütüphanesi bağımlılıkları kullanılan teknolojiler kısmında listelenmiştir. Bu kütüphanelere sahip değilseniz yüklemeniz gerekmektedir.
4.  **Model Dosyalarını Yerleştirme:** GitHub deposunu kopyaladıktan veya indirdikten sonra, projenizin ana dizininde aşağıdaki model dosyalarının bulunması **zorunludur**:
    * `kiyafet_modelim.h5`
    Aksi takdirde, `app.py` çalışırken “Model dosyası bulunamadı” hatası alırsınız.
5.  **Uygulamayı Başlatma:** Proje dizininizde iken `app.py` kodunu çalıştırın:
    ```bash
    python app.py
    ```
6.  **Web Arayüzüne Erişin:** Uygulama başarıyla başlatıldıktan sonra, terminaldeki "Running on http://..." linkine tıklayın.
7.  **Kullanım:** Ekranınızın orta kısmında bulunan "Görsel Seç" butonuyla görsel yükleyebilir ve "Tahmin Et" butonuyla da modelin tahminini görebilirsiniz.

---


# For English


# 👕 FashionDetector: Clothing Recognition App
