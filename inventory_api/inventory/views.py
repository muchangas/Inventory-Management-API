from rest_framework import generics, permissions
from .models import InventoryItem
from .serializers import InventoryItemSerializer

class InventoryItemListCreateView(generics.ListCreateAPIView):
    """
    GET: List all inventory items.
    POST: Create a new inventory item.
    Requires authentication.
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Overrides the default create method to set the added_by field 
        to the user making the request (self.request.user).
        """
        serializer.save(added_by=self.request.user)