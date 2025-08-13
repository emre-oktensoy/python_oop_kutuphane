# 📚 Python OOP Kütüphane Projesi

Bu proje, Python kullanılarak nesne yönelimli programlama (OOP) prensipleri ile geliştirilmiş bir kütüphane yönetim sistemi dlup üç aşamalı ve her aşamasında ayrı özellikler eklenerek geliştirilmiştir. Her aşama aşağıda belirtilmiştir.


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



