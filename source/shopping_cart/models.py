from django.db import models
from cookie_shop.settings import AUTH_USER_MODEL
from products.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.quantity} x {self.product.name} in {self.user.username}"
    
    
    def total_price(self):
        return self.quantity * self.product.price
    

class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cart for {self.user.username}"
    
    def total_quantity(self):
        total = 0
        for item in self.items.all():
            total += item.quantity
        return total