from django.contrib import admin
from sweets.models import Sweetshop
from django.contrib.admin.options import ModelAdmin

# Register your models here.
class SweetshopAdmin(ModelAdmin):
    search_fields = ["name"]
admin.site.register(Sweetshop,SweetshopAdmin)
