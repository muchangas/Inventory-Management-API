from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import InventoryItem

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class InventoryItemSerializer(serializers.ModelSerializer):
    added_by_username = serializers.ReadOnlyField(source='added_by.username')
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ['added_by', 'created_at', 'updated_at']

class LowStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = ['name', 'stock_level', 'reorder_point']