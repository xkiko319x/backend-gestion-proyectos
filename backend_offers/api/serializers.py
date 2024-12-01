from rest_framework import serializers
from .models import Company, Client, Responsible, Project, Offer, AuthUser

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class ResponsibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Responsible
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='project_client.client_name', read_only=True)
    responsible_name = serializers.CharField(source='project_responsible.responsible_name', read_only=True)

    class Meta:
        model = Project
        fields = ['project_id', 'project_name', 'client_name', 'project_budget', 'responsible_name']

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'email', 'name', 'rol', 'is_active', 'is_staff', 'rol']