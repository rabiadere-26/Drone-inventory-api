from django.db import models
from django.utils import timezone
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori")

    class Meta:
        verbose_name_plural = "Kategoriler"

    def __str__(self):
        return self.name

class Drone(models.Model):
    STATUS_CHOICES = [
        ('Hangarda', 'Hangarda'),
        ('Uçuşta', 'Uçuşta'),
        ('Bakımda', 'Bakımda'),
        ('Arızalı', 'Arızalı'),
    ]

    # İlişkili alanlar
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name='drones', 
        verbose_name="Kategori", 
        null=True, 
        blank=True
    )
    
    # Teknik Özellikler (Hepsi opsiyonel hale getirildi)
    name = models.CharField(max_length=100, verbose_name="İHA Adı")
    manufacturer = models.CharField(max_length=100, verbose_name="Üretici", null=True, blank=True)
    max_takeoff_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Azami Kalkış Ağırlığı (kg)", null=True, blank=True)
    payload_capacity = models.FloatField(verbose_name="Faydalı Yük Kapasitesi (kg)", null=True, blank=True)
    endurance = models.CharField(max_length=50, verbose_name="Havada Kalış", null=True, blank=True)
    range = models.CharField(max_length=100, verbose_name="Menzil / Kontrol", null=True, blank=True)
    altitude = models.CharField(max_length=100, verbose_name="İrtifa", null=True, blank=True)
    weapon_capability = models.TextField(verbose_name="Silah Kabiliyeti", blank=True, null=True)
    
    # Operasyonel Veriler
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Hangarda', verbose_name="Durum")
    total_flight_hours = models.FloatField(default=0, verbose_name="Toplam Uçuş Saati")
    last_maintenance_date = models.DateField(null=True, blank=True, verbose_name="Son Bakım Tarihi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kayıt Tarihi")

    class Meta:
        verbose_name_plural = "İHA'lar"

    def __str__(self):
        return f"{self.name} - {self.manufacturer if self.manufacturer else 'Bilinmiyor'}"
    

    @property
    def maintenance_status(self):
    # Senaryo 1: Uçuş saati 500'den fazlaysa
       if self.total_flight_hours >= 500:
        return "Kritik: Yüksek Uçuş Saati"
    
    # Senaryo 2: Son bakımdan 180 gün geçtiyse
       if self.last_maintenance_date:
        if timezone.now().date() - self.last_maintenance_date > timedelta(days=180):
            return "Uyarı: Bakım Süresi Geçti"
            
       return "Normal"