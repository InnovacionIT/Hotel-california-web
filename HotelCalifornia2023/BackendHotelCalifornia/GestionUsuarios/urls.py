from django.contrib import admin
from django.urls import path
from GestionUsuarios.views import ClienteCreateView, ClienteUpdateDelete
urlpatterns = [
    path('api/clientes/', ClienteCreateView.as_view()),
    path('api/clientes/<pk>/', ClienteUpdateDelete.as_view()),
]
