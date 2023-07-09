"""
from recipes.views import home

urlpatterns = [
    path('', home),
] A importação dessa forma seria mais trabalhosa, pois para importar outros
teria que fazer um a um como home, contato, etc. Assim importa-se o pacote
completo """

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),
]