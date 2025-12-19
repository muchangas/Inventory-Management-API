from rest_framework import serializers
from .models import InventoryItem

class InventoryItemSerializer(serializers.ModelSerializer):
    added_by_username = serializers.ReadOnlyField(source='added_by.username')
    
    class Meta:
        model = InventoryItem
        fields = [
            'id', 'name', 'description', 'price', 'stock_level', 
            'reorder_point', 'added_by', 'added_by_username', 
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'added_by', 'added_by_username', 'created_at', 'updated_at']

    def validate_stock_level(self, value):
        """Check that stock_level is not negative."""
        if value < 0:
            raise serializers.ValidationError("Stock level cannot be negative.")
        return value

    def validate_price(self, value):
        """Check that price is not negative."""
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value
class LowStockSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for displaying only essential low-stock data.
    """
    class Meta:
        model = InventoryItem
        fields = ['name', 'stock_level', 'reorder_point']