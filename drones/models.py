from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Kategori Adı") # İHA, SİHA, TİHA gibi

    def __str__(self):
        return self.name

class Drone(models.Model):
    STATUS_CHOICES = [
        ('Ucusda', 'Uçuşta'),
        ('Bakimda', 'Bakımda'),
        ('Hangarda', 'Hangarda'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='drones', verbose_name="Kategori", null=True)
    name = models.CharField(max_length=100, verbose_name="İHA Adı")
    model_series = models.CharField(max_length=50, verbose_name="Model Serisi")
    weight = models.FloatField(verbose_name="Ağırlık (kg)")
    payload_capacity = models.FloatField(verbose_name="Faydalı Yük Kapasitesi (kg)")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Hangarda')
    created_at = models.DateTimeField(auto_now_add=True)
    total_flight_hours = models.FloatField(default=0, verbose_name="Toplam Uçuş Saati")
    last_maintenance_date = models.DateField(null=True, blank=True, verbose_name="Son Bakım Tarihi")

    def __str__(self):
        return f"{self.name} ({self.category.name if self.category else 'Kategorisiz'})"