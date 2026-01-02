from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class InventoryItem(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_level = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=10)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name