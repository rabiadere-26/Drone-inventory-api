🛰️ Türkiye Menşeli İnsansız Hava Sistemleri (İHS) Envanter Takip Sistemi

Bu proje, Türkiye'nin yerli ve milli imkanlarla geliştirdiği İnsansız Hava Araçları'nın (İHA/SİHA) envanter takibini, operasyonel durumlarını ve teknik özelliklerini yönetmek için geliştirilmiş profesyonel bir Backend + Dashboard sistemidir.

🚀 Öne Çıkan Özellikler

Dinamik Envanter Yönetimi: İHA'lar, SİHA'lar, Hedef Uçaklar ve Döner Kanatlı sistemler için kategori bazlı yönetim.

Akıllı Bakım Takip Sistemi: Toplam uçuş saati ve son bakım tarihi verilerini işleyerek otomatik "Kritik" veya "Uyarı" durumları üreten iş mantığı (Business Logic).

Profesyonel API: Django REST Framework ile geliştirilmiş, tamamen dokümante edilmiş API uç noktaları.

İzlenebilirlik (Logging): Sistem üzerindeki tüm önemli hareketlerin ve hataların Python Logging modülü ile takip edilmesi.

Dockerize Mimari: docker-compose ile tek komutta ayağa kalkan PostgreSQL ve Web sunucusu entegrasyonu.

Otomatik Testler: Pytest ile %100 doğrulanan API ve Arayüz kararlılığı.

![İHS Envanter Dashboard](dashboard-ss.png)

🛠️ Teknik Altyapı

Backend: Django (Python 3.13)

Database: PostgreSQL

Frontend: Bootstrap 5 (Responsive Dashboard)

API Documentation: Swagger / OpenAPI 3.0 (drf-spectacular)

Testing: Pytest-Django

📦 Kurulum ve Çalıştırma

Sistemi yerel makinenizde çalıştırmak için Docker yüklü olması yeterlidir:

Projeyi klonlayın:

git clone https://github.com/kullaniciadi/ihs-envanter-sistemi.git
cd ihs-envanter-sistemi

Docker konteynerlerini ayağa kaldırın:

docker-compose up --build

Admin panelini kullanmak için superuser oluşturun:

docker-compose exec web python manage.py createsuperuser

Erişim Adresleri:

Dashboard: http://localhost:8000/dashboard/

API Docs (Swagger): http://localhost:8000/api/docs/

Admin Panel: http://localhost:8000/admin/

🧪 Testlerin Çalıştırılması

Sistemin kararlılığını doğrulamak için yazdığımız entegrasyon ve birim testlerini şu komutla çalıştırabilirsiniz:

docker-compose exec web pytest

📋 Örnek Senaryo: Akıllı Bakım Karar Mekanizması

Sistem, bir İHA'nın total_flight_hours verisi 500 saati geçtiğinde veya son bakımından bu yana 180 gün dolduğunda dashboard üzerinde görsel uyarılar oluşturur.

Not: Bu yapı, önleyici bakım (preventive maintenance) süreçlerinin dijitalleşmesini sağlar ve operasyonel hataları minimize eder.

🤝 İletişim
Bu proje, modern web teknolojileri ve savunma sanayii gereksinimleri temel alınarak geliştirilmiştir. Sorularınız için iletişime geçebilirsiniz.
