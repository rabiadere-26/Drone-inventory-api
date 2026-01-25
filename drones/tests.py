from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Drone, Category

class DroneTests(APITestCase):
    def setUp(self):
        # Test için geçici bir kategori ve drone oluşturuyoruz
        self.category = Category.objects.create(name="Test İHA")
        self.drone_data = {
            "name": "Test Drone",
            "model_series": "T1",
            "weight": 500.0,
            "payload_capacity": 100.0,
            "category": self.category.id,
            "status": "Hangarda"
        }

    def test_create_drone(self):
        """Drone oluşturma API'si çalışıyor mu?"""
        url = reverse('drone-list')
        response = self.client.post(url, self.drone_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Drone.objects.count(), 1)
        self.assertEqual(Drone.objects.get().name, 'Test Drone')

    def test_get_drones(self):
        """Drone listeleme API'si çalışıyor mu?"""
        url = reverse('drone-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.
