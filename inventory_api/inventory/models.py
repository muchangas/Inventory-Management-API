from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class InventoryItem(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Item Name")
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_level = models.IntegerField(default=0)
    reorder_point = models.IntegerField(default=10)

    added_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='inventory_items_added'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"

    def __str__(self):
        return f"{self.name} ({self.stock_level} in stock)"