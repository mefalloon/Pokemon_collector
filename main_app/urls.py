from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
    # route for pokemon index
  path('pokemon/', views.pokemon_index, name='index'),
]