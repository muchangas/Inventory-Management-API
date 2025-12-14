# inventory/urls.py

from django.urls import path
from .views import InventoryItemListCreateView, InventoryItemRetrieveUpdateDestroyView

urlpatterns = [
    # List/Create (GET, POST) -> /api/v1/inventory/items/
    path('items/', InventoryItemListCreateView.as_view(), name='item-list-create'),
    
    # Detail/Update/Destroy (GET, PUT, PATCH, DELETE) -> /api/v1/inventory/items/1/
    path('items/<int:pk>/', InventoryItemRetrieveUpdateDestroyView.as_view(), name='item-detail-update-destroy'),
]