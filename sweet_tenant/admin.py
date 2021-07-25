from django.contrib import admin

# Register your models here.
from .models import Sweet
# Register your models here.
@admin.register(Sweet)
class SweetTypeAdmin(admin.ModelAdmin):
    list_display=('name',)