from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_list(request):
    user = request.user
    if request.method == 'GET':
        if user.is_staff:
            if user.role == 'delivery_man':
                orders = Order.objects.filter(status__in=['en_preparacion', 'enviado'] )

            elif user.role == 'employee':
                orders = Order.objects.filter(status__in=['en_preparacion', 'pendiente'])
            
            elif user.role == 'manager':
                orders = Order.objects.all()
            
        else:
            orders = Order.objects.filter(user=user)
        
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([IsAuthenticated])
def order_detail(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response({'detail': 'Not found'}, status=404)
    
    # No permite ver pedidos de otros clientes
    if not request.user.is_staff and order.user != request.user:
        return Response({'detail': 'No tienes permiso para ver este pedido.'}, status=403)

    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)
        
    elif request.method == 'PUT':
        # No puedes cambiar estado si eres cliente
        if not request.user.is_staff:
            return Response({'detail': 'Acción denegada.'}, status=403)
            
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)