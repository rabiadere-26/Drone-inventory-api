from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import generics
from .models import Drone
from .serializers import DroneSerializer
from django.shortcuts import render
from .models import Drone, Category

# Bu sınıf tüm droneları listeler ve yeni drone eklenmesini sağlar (GET ve POST)
class DroneListCreate(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    filter_backends = [DjangoFilterBackend] # Filtrelemeyi ekledik
    filterset_fields = ['status', 'category']

# Bu sınıf tek bir drone'un detayını görür, günceller veya siler (GET, PUT, DELETE)
class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer


def dashboard(request):
    categories = Category.objects.prefetch_related('drones').all()
    return render(request, 'drones/dashboard.html', {'categories': categories})
# Create your views here.
