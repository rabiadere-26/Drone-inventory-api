import pytest
from django.urls import reverse
from rest_framework import status
from .models import Category, Drone

@pytest.mark.django_db
class TestDroneSystem:
    
    @pytest.fixture
    def setup_data(self):
        """Testler için başlangıç verisi oluşturur."""
        self.category = Category.objects.create(name="SİHA")
        self.drone_data = {
            "name": "Bayraktar TB2",
            "category": self.category.id,
            "manufacturer": "Baykar",
            "max_takeoff_weight": 700.00,
            "payload_capacity": 150.0,
            "endurance": "27 Saat",
            "range": "300 km",
            "altitude": "25.000 Feet",
            "status": "Hangarda",
            "total_flight_hours": 120.5
        }

    def test_dashboard_access(self, client, setup_data):
        """Dashboard sayfasının başarıyla açıldığını test eder."""
        url = reverse('dashboard')
        response = client.get(url)
        assert response.status_code == 200
        # Sayfada İHA isminin görünüp görünmediğini kontrol et
        assert "SİHA" in response.content.decode()

    def test_create_drone_api(self, client, setup_data):
        """API üzerinden yeni bir İHA eklenebildiğini test eder."""
        url = reverse('drone-list')  # drones.urls içindeki router adı 'drone' ise
        response = client.post(url, self.drone_data, format='json')
        
        assert response.status_code == status.HTTP_201_CREATED
        assert Drone.objects.count() == 1
        assert Drone.objects.get().name == "Bayraktar TB2"

    def test_drone_status_choices(self, setup_data):
        """Modeldeki varsayılan durumun doğru atandığını test eder."""
        drone = Drone.objects.create(
            name="Anka-S",
            category=self.category,
            manufacturer="TUSAŞ",
            max_takeoff_weight=1500,
            payload_capacity=200,
            endurance="24 Saat",
            range="250 km",
            altitude="30.000 Feet"
        )
        assert drone.status == 'Hangarda'  # Default değer testimiz