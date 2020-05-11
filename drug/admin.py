from django.contrib import admin
from .models import DrugItem, DrugCategory

# Register your models here.
admin.site.register(DrugCategory)
admin.site.register(DrugItem)