from django.contrib import admin 
from .models import kumbi
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.admin.models import LogEntry

# Register your models here.

class KumbiAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email","password","confirmPassword","dob","gender",)


admin.site.register(kumbi,KumbiAdmin)

# create cutom user class

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

admin.site.register(CustomUser, CustomUserAdmin)