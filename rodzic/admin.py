from django.contrib import admin
from .models import Rodzic, Dziecko
# Register your models here.


class DzieckoAdmin(admin.ModelAdmin):
    list_display = ['imie', 'nazwisko']
    search_fields = ['imie', 'nazwisko']
    ordering = ['nazwisko', 'imie']

class RodzicAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dziecko, DzieckoAdmin)
admin.site.register(Rodzic, RodzicAdmin)