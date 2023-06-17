from django.shortcuts import render

# Importa las clases necesarias de Django REST Framework y tus archivos locales
from rest_framework import generics
from .models import Cliente
from .serializers import ClienteSerializer

# Vista para listar y crear clientes
class ClienteListCreateView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()   # Obtiene todos los clientes de la base de datos
    serializer_class = ClienteSerializer   # Usa el serializador ClienteSerializer para convertir los datos en formato JSON

# Vista para obtener, actualizar y eliminar un cliente específico
class ClienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()   # Obtiene todos los clientes de la base de datos
    serializer_class = ClienteSerializer   # Usa el serializador ClienteSerializer para convertir los datos en formato JSON
