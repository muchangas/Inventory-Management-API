from django.db import models
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Import your local models, serializers, and permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer, UserSerializer, LowStockSerializer
from .permissions import IsOwnerOrReadOnly

# --- USER MANAGEMENT ---

class UserRegistrationView(APIView):
    """
    Endpoint to allow new users to register.
    Accessible by anyone (AllowAny).
    """
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# --- INVENTORY MANAGEMENT ---

class InventoryItemListCreateView(generics.ListCreateAPIView):
    """
    Handles GET (List) and POST (Create) for Inventory Items.
    Automatically assigns the logged-in user to the 'added_by' field.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # This line prevents the 500 error by linking the item to the user
        serializer.save(added_by=self.request.user)


class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET, PUT, PATCH, and DELETE for a single item.
    Uses custom permission 'IsOwnerOrReadOnly' to protect data.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]


class LowInventoryListView(generics.ListAPIView):
    """
    A specialized read-only endpoint that returns items 
    where the stock_level is at or below the reorder_point.
    """
    serializer_class = LowStockSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Using F() allows us to compare two fields on the same row
        return InventoryItem.objects.filter(stock_level__lte=models.F('reorder_point'))