from django.contrib import admin
from django.urls import path, include
from games.views import *
urlpatterns = [
    path('', home_page, name='home-page'),
    path('dashboard/', dashboard, name='dashboard'),

    path('profile/create/', create_profile, name='create-profile'),
    path('profile/details/', details_profile, name='details-profile'),
    path('profile/edit/', edit_profile, name='edit-profile'),
    path('profile/delete/', delete_profile, name='delete-profile'),

    
    path('game/create/', game_create, name='game-create'),
    path('game/details/<int:id>/', game_details, name='game-details'),
    path('game/edit/<int:id>/', game_edit, name='game-edit'),
    path('game/delete/<int:id>/', game_delete, name='game-delete'),
]
