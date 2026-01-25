# 🛸 İHA Envanter Yönetim Sistemi 

Bu proje, İnsansız Hava Araçları (İHA) ve Silahlı İnsansız Hava Araçlarının (SİHA) envanter takibini yapmak, teknik verilerini yönetmek ve operasyonel durumlarını izlemek için geliştirilmiş bir **Backend API** çalışmasıdır.

## 🚀 Öne Çıkan Özellikler
- **RESTful API:** Django REST Framework kullanılarak geliştirilen tam kapsamlı CRUD operasyonları.
- **Relational Database:** İHA ve SİHA kategorileri arasında ilişkisel (Foreign Key) mimari.
- **Havacı Mantığı:** Araçlar için "Toplam Uçuş Saati" ve "Son Bakım Tarihi" gibi sektörel veri alanları.
- **Interaktif Dokümantasyon:** Swagger (OpenAPI 3) üzerinden anlık API testi imkanı.
- **Dashboard:** Operasyonel takip için Bootstrap tabanlı izleme paneli.
- **Konteynerizasyon:** Docker ve Docker-Compose desteği.

## 🛠 Kullanılan Teknolojiler
- **Dil:** Python 3.13
- **Framework:** Django 5.x, Django REST Framework
- **Veritabanı:** SQLite (Geliştirme aşaması için)
- **Konteyner:** Docker, Docker-Compose
- **Dokümantasyon:** Drf-spectacular (Swagger)

## 📦 Kurulum ve Çalıştırma

### 1. Yerel Geliştirme Ortamı
Projeyi kendi bilgisayarınızda çalıştırmak için:

# Sanal ortam oluşturma
python -m venv venv

# Sanal ortamı aktif etme (Windows)
venv\Scripts\activate

# Bağımlılıkları yükleme
pip install -r requirements.txt

# Veritabanını hazırlama
python manage.py migrate

# Sunucuyu başlatma
python manage.py runserver

Uygulama varsayılan olarak http://127.0.0.1:8000/ adresinde çalışacaktır.

### Docker ile Çalıştırma (Önerilen)

docker-compose up --build

🔗 Önemli Endpointler
Proje ayağa kalktıktan sonra aşağıdaki adreslerden test edilebilir:

API Dashboard (Görsel İzleme): http://localhost:8000/api/dashboard/

Swagger Dokümantasyonu: http://localhost:8000/api/docs/

İHA Listesi (JSON API): http://localhost:8000/api/drones/

🧪 Testler
Sistemdeki API endpoint'lerinin ve iş mantığının doğruluğunu kontrol etmek için hazırlanan testleri şu komutla çalıştırabilirsiniz:

python manage.py test