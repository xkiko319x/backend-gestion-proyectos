# backend_offers/api/views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets
from .models import Company, Client, Responsible, Project, Offer, AuthUser
from .serializers import CompanySerializer, ClientSerializer, ResponsibleSerializer, ProjectSerializer, OfferSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AuthUserSerializer

class LoginView(APIView):  
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_data = AuthUserSerializer(user).data
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    **user_data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"message": "Credenciales inválidas"},
                status=status.HTTP_401_UNAUTHORIZED
            )

class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthUserSerializer

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
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            new_project = Project.objects.create(
                project_name=data.get('project_name'),
                project_budget=data.get('project_budget'),
                project_client_id=data.get('project_client'),
                project_responsible_id=data.get('project_responsible'),
            )
            serializer = self.get_serializer(new_project)

            return Response(
                {"message": "Project created successfully!", "project": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def update(self, request, *args, **kwargs):
        data = request.data
        project_id = kwargs.get('pk')
        
        try:
            project = Project.objects.get(project_id=project_id)
            client = Client.objects.get(client_name=data.get('client_name'))  
            responsible = Responsible.objects.get(responsible_name=data.get('responsible_name'))  

            project.project_name = data.get('project_name', project.project_name) 
            project.project_budget = data.get('project_budget', project.project_budget)
            project.project_client = client
            project.project_responsible = responsible 
            project.save() 

            serializer = self.get_serializer(project)
            return Response(
                {"message": "Project updated successfully!", "project": serializer.data},
                status=status.HTTP_200_OK
            )
        except Project.DoesNotExist:
            return Response(
                {"error": "Project not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Client.DoesNotExist:
            return Response(
                {"error": "Client with the given name not found."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Responsible.DoesNotExist:
            return Response(
                {"error": "Responsible with the given name not found."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
    
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer

    def get(self, request):
        offers = Project.objects.all()
        serializer = OfferSerializer(offers, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        try:
            new_offer = Offer.objects.create(
                offer_title=data.get('offer_title'),
                offer_reference=data.get('offer_reference'),
                offer_amount=data.get('offer_amount'),
                offer_responsible_id=data.get('offer_responsible'),
                offer_project_id=data.get('offer_project'),
                offer_client_id=data.get('offer_client'),
                offer_company_id=data.get('offer_company'),
            )
            serializer = self.get_serializer(new_offer)

            return Response(
                {"message": "Offer created successfully!", "offer": serializer.data},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        
    def update(self, request, *args, **kwargs):
        data = request.data
        offer_id = kwargs.get('pk')
        try:
            offer = Offer.objects.get(offer_id=offer_id)

            client = Client.objects.get(client_name=data.get('client_name'))  
            responsible = Responsible.objects.get(responsible_name=data.get('responsible_name')) 
            project = Project.objects.get(project_name=data.get('project_name'))
            company = Company.objects.get(company_name=data.get('company_name'))

            # Actualizar los campos del proyecto
            offer.offer_title = data.get('offer_title', offer.offer_title) 
            offer.offer_amount = data.get('offer_budget', offer.offer_amount)
            offer.offer_reference = data.get('offer_reference', offer.offer_reference) 
            offer.offer_reference = data.get('offer_reference', offer.offer_reference) 
            offer.offer_client = client  
            offer.offer_responsible = responsible  
            offer.offer_company = company  
            offer.offer_project = project  
            
            offer.save()

            serializer = self.get_serializer(offer)
            return Response(
                {"message": "offer updated successfully!", "offer": serializer.data},
                status=status.HTTP_200_OK
            )
        except offer.DoesNotExist:
            return Response(
                {"error": "offer not found."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Client.DoesNotExist:
            return Response(
                {"error": "Client with the given name not found."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Responsible.DoesNotExist:
            return Response(
                {"error": "Responsible with the given name not found."},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )