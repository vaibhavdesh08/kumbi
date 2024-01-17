from django.contrib import admin 
from .models import kumbi


# Register your models here.

class KumbiAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email","password","confirmPassword","dob","gender",)


admin.site.register(kumbi,KumbiAdmin)
