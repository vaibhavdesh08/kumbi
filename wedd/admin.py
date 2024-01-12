from django.contrib import admin
from .models import wandekar

# Register your models here.

class WandekarAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email","password","confirmPassword","dob","gender",)

admin.site.register(wandekar,WandekarAdmin )