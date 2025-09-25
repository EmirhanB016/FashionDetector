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
| ![Uygulama Arayüzü](images/uygulama_arayuzu.png) | ![Tahmin Demousu]() |

---
