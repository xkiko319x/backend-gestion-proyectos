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
    client_name = serializers.CharField(source='offer_client.client_name', read_only=True)
    company_name = serializers.CharField(source='offer_company.company_name', read_only=True)
    project_name = serializers.CharField(source='offer_project.project_name', read_only=True)
    responsible_name = serializers.CharField(source='offer_responsible.responsible_name', read_only=True)

    class Meta:
        model = Offer
        fields = [
                    'offer_id',
                    'offer_title',
                    'offer_reference',
                    'offer_amount',
                    'responsible_name',
                    'project_name',
                    'company_name',
                    'client_name'
                ]
class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'username', 'email', 'name', 'rol', 'is_active', 'is_staff', 'rol']
