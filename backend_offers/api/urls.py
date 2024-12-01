from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, CompanyViewSet, ClientViewSet, ResponsibleViewSet, ProjectViewSet, OfferViewSet, AuthUserViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'responsibles', ResponsibleViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'offers', OfferViewSet)
router.register(r'users', AuthUserViewSet)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
]

