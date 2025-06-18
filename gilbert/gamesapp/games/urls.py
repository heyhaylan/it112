from django.urls import path
from . import views

urlpatterns = [
    path('', views.game_list, name='game_list'),
    path('game/<int:pk>/', views.game_detail, name='game_detail'),
    path('api/games/', views.api_get_all, name='api_get_all'),
    path('api/game/', views.api_get_game_by_id, name='api_get_game'),
    path('api/game/create/', views.api_create_game, name='api_create_game'),
]
