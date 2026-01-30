from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import generics
from .models import Drone
from .serializers import DroneSerializer
import logging
from django.shortcuts import render
from .models import Category

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

logger = logging.getLogger(__name__)


def dashboard(request):
    try:
        categories = Category.objects.all()
        # Bilgi mesajı yazdıralım
        logger.info(f"Dashboard sayfası {request.user} tarafından görüntülendi.")
        
        return render(request, 'drones/dashboard.html', {'categories': categories})
    
    except Exception as e:
        # Hata mesajını sisteme kaydet
        logger.error(f"Dashboard açılırken bir hata oluştu: {str(e)}")
        raise e
