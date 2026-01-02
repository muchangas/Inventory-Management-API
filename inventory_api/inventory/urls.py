from django.urls import path
from .views import (
    InventoryItemListCreateView, 
    InventoryItemDetailView, 
    LowInventoryListView, 
    UserRegistrationView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('items/', InventoryItemListCreateView.as_view(), name='item-list'),
    path('items/<int:pk>/', InventoryItemDetailView.as_view(), name='item-detail'),
    path('levels/', LowInventoryListView.as_view(), name='low-stock'),
]