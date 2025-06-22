from django.contrib import admin
from .models import Game

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'studio', 'release_year')
    search_fields = ('title', 'studio')                 
    list_filter = ('release_year',)                          