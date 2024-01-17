from django.contrib import admin
from main.models import Phone


@admin.register(Phone)
class Contact(admin.ModelAdmin):
    pass