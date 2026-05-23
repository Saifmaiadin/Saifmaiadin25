# suppliers/models.py
from django.db import models
from locations.models import Location

class SupplierCategory(models.TextChoices):
    RAW_MATERIAL = 'raw', 'مواد خام'
    EQUIPMENT = 'equip', 'معدات وآلات'
    SERVICE = 'service', 'خدمات'
    LOGISTICS = 'logistics', 'خدمات لوجستية'

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=SupplierCategory.choices)
    tax_id = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    payment_terms = models.IntegerField(default=30)  # أيام السداد
    is_active = models.BooleanField(default=True)
    # الربط بالمواقع: المورد يمكن أن يخدم عدة فروع (علاقة كثير لكثير)
    branches = models.ManyToManyField(Location, related_name='suppliers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name