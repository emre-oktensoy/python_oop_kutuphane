# 📚 Python OOP Kütüphane Projesi

Bu proje, Python kullanılarak nesne yönelimli programlama (OOP) prensipleri ile geliştirilmiş bir kütüphane yönetim sistemi olup üç aşamalı ve her aşamasında projeye ayrı özellikler eklenmiştir. Aşamalara ilişkin bilgiler aşağıda belirtilmiştir.

# Proje Aşama-3

# 🚀 Özellikler
- Kütüphane verilerine bir web arayüzü (API) üzerinden erişim sağlamak
- Kitap ekleme, silme, listeleme işlemleri endpoint metodlar ile yapılıyor
- Testler (pytest ile)
- Open Library Books API kullanılarak kitap bilgisinin alınması ve json dosyasına kayıt işlemi
- Pydantic ile veri doğrulama 

# 📦 Kurulum

  # Sanal ortam oluştur
  python -m venv venv
  
  # Sanal ortamı aktifleştir (Mac)
  source venv/bin/activate
  # Sanal ortamı aktifleştir (Windows)
  .\.venv\Scripts\activate
  
  # Gerekli paketleri yükle
  pip install -r requirements.txt

# ▶️ Çalıştırma
uvicorn api:app --reload

API Endpoint Listesi – Library API

  🔹 GET /books
- Amaç: Kütüphanedeki tüm kitapları listeler.
- Yanıt: JSON formatında kitap listesi.

🔹 POST /books
- Amaç: ISBN numarasına göre Open Library API'den kitap bilgisi alır ve kütüphaneye ekler.
- Örnek Body Yapısı:{"isbn": "9780140328721"}
- Yanıt: Eklenen kitabın bilgileri.

🔹DELETE /books/{isbn}
- Amaç: Belirtilen ISBN numarasına sahip kitabı kütüphaneden siler.
- Parametre: isbn (örneğin: 9780140328721)
- Yanıt: 204 No Content (başarılı silme) 


# 🧪 Test Çalıştırma
 pytest .\test_api.py
 
<img width="1913" height="940" alt="image" src="https://github.com/user-attachments/assets/4294d90f-64e6-43d1-9ce6-09bfc695c7fb" />
<img width="1554" height="981" alt="image" src="https://github.com/user-attachments/assets/83eb61a4-c81f-44b8-b0af-a977905b3144" />
<img width="1469" height="965" alt="image" src="https://github.com/user-attachments/assets/fb9bfbac-cc90-4962-81ce-bb70bb024981" />
<img width="1460" height="909" alt="image" src="https://github.com/user-attachments/assets/0cdb63e1-5870-4bc3-b083-fecf7a018129" />


# Proje Aşama-2

# 🚀 Özellikler
- Kitap ekleme, silme, listeleme
- Testler (pytest ile)
- Open Library Books API kullanılarak kitap bilgisinin alınması ve json dosyasına kayıt işlemi
- Pydantic ile veri doğrulama 

# 📦 Kurulum

  # Sanal ortam oluştur
  python -m venv venv
  
  # Sanal ortamı aktifleştir (Mac)
  source venv/bin/activate
  # Sanal ortamı aktifleştir (Windows)
  .\.venv\Scripts\activate
  
  # Gerekli paketleri yükle
  pip install -r requirements.txt

# ▶️ Çalıştırma
python main.py

# 🧪 Test Çalıştırma
 pytest .\test_library.py


# Proje Aşama-1

# 🚀 Özellikler
- Kitap ekleme, silme, listeleme
- E-kitap ve sesli kitap türleri
- Testler (pytest ile)
- Kullanıcıdan alınan kitap bilgilerinin json dosyasına kayıt işlemi

# 📦 Kurulum

  # Sanal ortam oluştur
  python -m venv venv
  
  # Sanal ortamı aktifleştir (Mac)
  source venv/bin/activate
  # Sanal ortamı aktifleştir (Windows)
  .\.venv\Scripts\activate
  
  # Gerekli paketleri yükle
  pip install pydantic pytest

# ▶️ Çalıştırma
python main.py

# 🧪 Test Çalıştırma
 pytest .\test_library.py



