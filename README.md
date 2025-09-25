# 👕 FashionDetector: Kıyafet Tespit Uygulaması
> NOT: Bu projede "Fashion-MNIST" veri seti kullanılmış ve proje yapay zeka yardımıyla yapılmıştır!!!

---

## 💡 Proje Hakkında
Bu proje, **derin öğrenme (Deep Learning)** tekniklerini kullanarak yüklediğiniz kıyafet fotoğraflarının "**Tişört**", "**Elbise**", "**Spor Ayakkabı**", "**Çanta**" gibi kategorilerinden hangisine ait olduğunu belirleyen bir **web uygulamasıdır**. `FashionDetector` adını taşıyan bu uygulama, kullanıcıların yüklediği kıyafet fotoğraflarının hangi kategoriye ait olduğunu yapay zeka yardımıyla tahmin etmeyi amaçlar.

### 🌟 Temel Hedef:
* Kullanıcıların kıyafetlerin ne olduğunu kolayca tahmin etmesini sağlamak.
---

## ✨ Özellikler

* **Gerçek Zamanlı Tahmin:** Kullanıcıların yüklediği kıyafet fotoğrafına göre model, resmi **AJAX** kullanarak tahminin sayfa yenilenmeden anında gösterilmesini sağlar
* **Kullanıcı Dostu Web Arayüzü:** HTML sayfası üzerinden fotoğraf yükleme, ve “Tahmin Et” butonu ile kolay bir kullanım sunar.
* **API Entegrasyonu:** `/tahmin` uç noktası üzerinden dosya kabul edilir, model tahmini yapar ve yapılan tahmini döndürür.

---

