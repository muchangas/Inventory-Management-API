from django.urls import path
from .views import InventoryItemListCreateView

urlpatterns = [
    path('items/', InventoryItemListCreateView.as_view(), name='item-list-create'),
]