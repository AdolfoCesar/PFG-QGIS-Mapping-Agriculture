from django.contrib import admin
from .models import Parcelas
#from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class ParcelasAdmin(admin.ModelAdmin):
    pass
    #list_display =('nombre','parcela')

admin.site.register(Parcelas, ParcelasAdmin)