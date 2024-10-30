from django.urls import path
from .views import menu, modificar,eliminar,lista_productos

urlpatterns =[
    path('menu/', menu, name='menu'),
    path('modificar/<id>/', modificar, name='modificar'),
    path('eliminar/<id>/', eliminar, name='eliminar'),
    path('lista_productos/',lista_productos, name='lista_productos'),
]