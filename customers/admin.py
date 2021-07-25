from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import Client

admin.site.register(Client)
