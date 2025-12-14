# inventory/views.py

from django.db import models # <-- ADDED: Needed for models.F()
from rest_framework import generics, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer, LowStockSerializer # <-- CORRECTED: Import LowStockSerializer

# 1. Inventory Item List and Create
class InventoryItemListCreateView(generics.ListCreateAPIView):
    """
    GET: List all inventory items. POST: Create a new inventory item.
    Requires authentication.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

# 2. Inventory Item Detail, Update, and Destroy
class InventoryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve details, PUT/PATCH: Update, DELETE: Destroy.
    Requires authentication.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

# 3. Low Inventory List View
class LowInventoryListView(generics.ListAPIView):
    """
    GET: List all inventory items that are below their reorder point (Low Stock).
    Requires authentication.
    """
    serializer_class = LowStockSerializer # <-- Now correctly defined and imported
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filter items where stock_level is less than or equal to reorder_point
        # models.F() is now available because we imported django.db.models
        return InventoryItem.objects.filter(stock_level__lte=models.F('reorder_point'))