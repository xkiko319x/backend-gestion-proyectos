# backend_offers/api/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from .models import Company, Client, Responsible, Project, Offer
from .serializers import CompanySerializer, ClientSerializer, ResponsibleSerializer, ProjectSerializer, OfferSerializer

class LoginView(APIView):  # Usa APIView en lugar de View
    def post(self, request):
        username = request.data.get('username')  # Cambiado a request.data
        password = request.data.get('password')  # Cambiado a request.data
        user = authenticate(request, username=username, password=password)
        
        print(f'Username: {username}, Password: {password}')
        print(f'Authenticated User: {user}')

        if user is not None:
            login(request, user)
            return Response({"message": "Inicio de sesión exitoso!"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Credenciales inválidas"}, status=status.HTTP_401_UNAUTHORIZED)

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ResponsibleViewSet(viewsets.ModelViewSet):
    queryset = Responsible.objects.all()
    serializer_class = ResponsibleSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer