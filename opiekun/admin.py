from django.contrib import admin

from .models import Grupa, Opiekun

class GrupaAdmin(admin.ModelAdmin):
    list_display = ['nazwa', 'rocznik']
    search_fields = ['nazwa', 'rocznik']
    ordering = ['rocznik', 'nazwa']

class OpiekunAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['user']


admin.site.register(Grupa, GrupaAdmin)
admin.site.register(Opiekun, OpiekunAdmin)

