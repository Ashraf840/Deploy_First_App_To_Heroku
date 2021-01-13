from django.contrib import admin
from .models import *



# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'phone', 'email']
    list_display_links = ['name']
    search_fields = ['id', 'name', 'roll', 'phone', 'email']
    list_per_page = 5


admin.site.register(Student, StudentAdmin)