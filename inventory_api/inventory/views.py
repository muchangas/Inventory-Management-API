from django.db import models
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import InventoryItem
from .serializers import InventoryItemSerializer, UserSerializer, LowStockSerializer
from .permissions import IsOwnerOrReadOnly

class UserRegistrationView(APIView):
    permission_classes = [permissions.AllowAny]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InventoryItemListCreateView(generics.ListCreateAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)

class InventoryItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

class LowInventoryListView(generics.ListAPIView):
    serializer_class = LowStockSerializer
    def get_queryset(self):
        return InventoryItem.objects.filter(stock_level__lte=models.F('reorder_point'))