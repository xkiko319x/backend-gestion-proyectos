from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)

class AuthUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, default='')
    rol = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'name', 'rol']  # Aquí defines los campos requeridos

    def __str__(self):
        return self.username

# api/models.py
from django.db import models

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_reference = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    client_reference = models.CharField(max_length=255)

    def __str__(self):
        return self.client_name

class Responsible(models.Model):
    responsible_id = models.AutoField(primary_key=True)
    responsible_user_id = models.IntegerField()
    responsible_name = models.CharField(max_length=255)
    responsible_username = models.CharField(max_length=255)

    def __str__(self):
        return self.responsible_name

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=255)
    project_responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    project_client = models.CharField(max_length=255)
    project_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.project_name

class Offer(models.Model):
    offer_id = models.AutoField(primary_key=True)
    offer_title = models.CharField(max_length=255)
    offer_reference = models.CharField(max_length=255)
    offer_amount = models.DecimalField(max_digits=10, decimal_places=2)
    offer_responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    offer_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    offer_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    offer_client_company = models.CharField(max_length=255)

    def __str__(self):
        return self.offer_title








# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class AuthUser(AbstractUser):  # Cambiar a heredar de AbstractUser
#     rol = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username  # Representación legible del objeto
