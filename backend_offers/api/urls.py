# backend_offers/api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, CompanyViewSet, ClientViewSet, ResponsibleViewSet, ProjectViewSet, OfferViewSet

# Crear el router y registrar las vistas
router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'responsibles', ResponsibleViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'offers', OfferViewSet)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),  # Agrega las rutas de CRUD para los modelos
]
