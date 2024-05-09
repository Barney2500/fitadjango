from django.contrib import admin
from .models import Automobil, Reservas

class ReservasInline(admin.TabularInline):
    model = Reservas
    extra = 1  # Cuántos formularios vacíos para reservas mostrar de inicio

@admin.register(Automobil)
class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')
    inlines = [ReservasInline]

@admin.register(Reservas)
class ReservasAdmin(admin.ModelAdmin):
    list_display = ('auto', 'usuari', 'inici', 'final')
    list_filter = ('auto', 'usuari', 'inici')
    search_fields = ('auto__marca', 'auto__model', 'usuari__username', 'inici', 'final')

