from django.contrib import admin
from django.urls import path
from .views import ClienteListCreateView, ClienteRetrieveUpdateDestroyView

urlpatterns = [
    path('Clientes/', ClienteListCreateView.as_view(), name='cliente-list-create'),
    path('Clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view(), name='cliente-retrieve-update-destroy'),
]
