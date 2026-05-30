from rest_framework import serializers
from .models import Order, OrderDetail
from users.models import Address

class AddressSerializer(serializers.ModelSerializer):
    inline_address = serializers.SerializerMethodField()

    class Meta:
        model = Address
        fields = '__all__'

    def get_inline_address(self, obj):
        # Genera string de la direccion
        piso = f", {obj.floor_door}" if obj.floor_door else ""
        return f"{obj.street} Nº {obj.number}{piso}, {obj.post_code}, {obj.city}"


class OrderDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    subtotal = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderDetail
        fields = '__all__'  


class OrderSerializer(serializers.ModelSerializer):
    # Anidamos las líneas del producto usando el related_name='details' 
    details = OrderDetailSerializer(many=True, read_only=True)
    # Extraemos el nombre completo del cliente
    client_name = serializers.CharField(source='user.get_full_name', read_only=True)
    # Sobrescribimos el campo original 'address' para que mande el JSON 
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'  