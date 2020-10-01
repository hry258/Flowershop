from django.contrib import admin
from flower.models import Flower

# Register your models here.

class FlowerAdmin(admin.ModelAdmin):
    list_display = ['nume', 'poza', 'pret', 'descriere', 'stoc']

admin.site.register(Flower, FlowerAdmin)