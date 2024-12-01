from django.contrib import admin
from .models import AuthUser, Company,Client,Responsible,Project,Offer

admin.site.register(AuthUser)
admin.site.register(Company)
admin.site.register(Client)
admin.site.register(Responsible)
admin.site.register(Project)
admin.site.register(Offer)