from django.contrib import admin
from .models import Fintastic

class FintasticAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')

# Register your models here.

admin.site.register(Fintastic, FintasticAdmin)