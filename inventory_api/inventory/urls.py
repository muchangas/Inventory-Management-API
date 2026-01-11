from django.urls import path
from .views import (
    InventoryItemListCreateView, 
    InventoryItemDetailView, 
    LowInventoryListView, 
    UserRegistrationView
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('items/', InventoryItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', InventoryItemDetailView.as_view(), name='item-detail'),
    path('levels/', LowInventoryListView.as_view(), name='low-stock'),
]

from django.urls import path
from .views import InventoryItemListCreateView, LowInventoryListView, UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()), # results in /register/
    path('items/', InventoryItemListCreateView.as_view()), # results in /items/
    path('levels/', LowInventoryListView.as_view()), # results in /levels/
]