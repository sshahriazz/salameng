from django.contrib import admin
from .models import AC, AcCategory, FridgeCategory, Fridge, ElectricProductCategory, ElectricProduct
# Register your models here.
admin.site.register(AC)
admin.site.register(AcCategory)
admin.site.register(FridgeCategory)
admin.site.register(Fridge)
admin.site.register(ElectricProductCategory)
admin.site.register(ElectricProduct)