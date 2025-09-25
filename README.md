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
> NOTE: The “Fashion-MNIST” dataset was used in this project, and the project was completed with the help of artificial intelligence!!!

---

## 💡 Project Details
This project is a **web application** that uses **deep learning** techniques to determine which category your uploaded clothing photos belong to, such as “**T-shirt**”, “**Dress**”, “**Sneakers**” or “**Bag**”. This application, named `FashionDetector`, aims to predict which category uploaded clothing photos belong to using artificial intelligence.

### 🌟 Temel Hedef:
* Kullanıcıların kıyafetlerin ne olduğunu kolayca tahmin etmesini sağlamak.
---

## ✨ Features

* **Real-Time Prediction:** Based on the clothing photo uploaded by users, the model uses **AJAX** to display the prediction instantly without refreshing the page.
* **User-Friendly Web Interface:** Allows photo uploads via an HTML page and offers easy usage with the “Tahmin Et” button.
* **API Integration:** Files are accepted via the `/tahmin` endpoint, which makes predictions using an artificial intelligence model and returns the name of the predicted garment as a result.
---
## 🚀 Quick Start & Demo

Curious about how the app works? Here's a quick overview and demos:

1.  **Start the Application:** Follow the steps in the “Installation and Running” section to run the `app.py` file.
2.  **Open the Web Interface:** Click the “Running on http://...” link in the terminal.
3.  **Upload a Photo:** Upload a photo of an outfit to the interface and see the prediction result instantly!

| Application Interface                  | Prediction Result Demo                      |
| :------------------------------------- | :------------------------------------------ |
| ![Uygulama Arayüzü](images/uygulama_arayuzu.png) | ![Tahmin Demousu](images/uygulama_demo.gif) |

---

## 🛠️ Technologies and Libraries Used

The following technologies and Python libraries were used during the development of this project:

* **Python:** It has been used as the main programming language of the project.
* **Flask:** It has been used to create a simple web server and API.
* **TensorFlow / Keras:** Used for loading a pre-trained deep learning model in `.h5` format and performing prediction operations.
* **Pillow:** It is used to read photo data from the user and perform appropriate resizing and preprocessing steps.
* **NumPy:** It is used to convert image data into numerical arrays and perform the necessary mathematical operations on these arrays.

### 📊 Data Sources

* Each of the clothing photos used in the project was taken from the “Fashion-MNIST” dataset.

---

## ⚙️ Installation and Running

To get your project working in your local environment, you can follow these steps:

1.  **Cloning the Project:** Download or clone the project from GitHub.   
2.  **Python Version Check:** Ensure that **Python 3.8-3.10** is installed on your system. 
3.  **Installing Dependencies:** All Python library dependencies for the project are listed in the technologies section. If you do not have these libraries, you will need to install them.
4.  **Placing Model Files:** After copying or downloading the GitHub repository, the following model files **must** be present in your project's root directory:
    * `kiyafet_modelim.h5`
    Otherwise, you will receive a “Model file not found” error when running `app.py`.
5.  **Starting the Application:** While in your project directory, run the `app.py` code:
    ```bash
    python app.py
    ```
6.  **Access the Web Interface:** After the application has successfully started, click the “Running on http://...” link in the terminal.
7.  **Usage:** You can upload an image using the “Select Image” button in the middle of your screen and view the model's prediction using the “Predict” button.
