from rest_framework import serializers
from .models import Product, Category, Allergen

class AllergenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allergen
        fields = ['name', 'image']

class ProductSerializer(serializers.ModelSerializer):
    allergens = AllergenSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'