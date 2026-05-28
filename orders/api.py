from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import OrderSerializer
# TODO:
# ENDPOINT PARA GESTIONAR EL ESTADO DEL PEDIDO
# ENDPOINT PARA CREAR EL PEDIDO EN EL CARRITO

# Este archivo gestiona las respuestas api que pedira react para poder dibujar
# la información de los estados de pedidos y poder cambiarlos

#Crear y listar pedidos
@api_view(['GET', 'POST'])
def order_list(request):
    pass

@api_view(['GET','PUT', 'DELETE'])
def order_detail(request):
    pass