from django.db import models
from rest_framework import generics, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer, LowStockSerializer # <-- CORRECTED: Import LowStockSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from .permissions import IsOwnerOrReadOnly
class InventoryItemListCreateView(generics.ListCreateAPIView):
    """
    GET: List all inventory items. POST: Create a new inventory item.
    Requires authentication.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)
class InventoryItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve details, PUT/PATCH: Update, DELETE: Destroy.
    Requires authentication.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]
class LowInventoryListView(generics.ListAPIView):
    """
    GET: List all inventory items that are below their reorder point (Low Stock).
    Requires authentication.
    """
    serializer_class = LowStockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return InventoryItem.objects.filter(stock_level__lte=models.F('reorder_point'))
    
class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny] # Public endpoint

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)