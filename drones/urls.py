from django.urls import path
from .views import DroneListCreate, DroneDetail
from .views import DroneListCreate, DroneDetail, dashboard # dashboard'u ekledik

urlpatterns = [
    path('drones/', DroneListCreate.as_view(), name='drone-list'),
    path('drones/<int:pk>/', DroneDetail.as_view(), name='drone-detail'),
]

urlpatterns = [
    path('drones/', DroneListCreate.as_view(), name='drone-list'),
    path('drones/<int:pk>/', DroneDetail.as_view(), name='drone-detail'),
    path('dashboard/', dashboard, name='dashboard'), # Bunu ekledik
]