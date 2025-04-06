from rest_framework import serializers
from .models import Category, Product, Order
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()  # Display category name

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Order
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

