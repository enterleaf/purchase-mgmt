import uuid
from django.db import models
from apps.supplier_mgmt.models import Supplier, Address
from .choices import OrderStatus, PaymentTerms, PaymentMethod, ShippingMethod


class Order(models.Model):
    order_number = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_date = models.DateField()
    # order_number = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    order_status = models.CharField(
        max_length=20, choices=OrderStatus.choices, default=OrderStatus.DRAFT
    )
    supplier_name = models.CharField(max_length=255)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity_ordered = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_category = models.CharField(max_length=255)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    tax = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    payment_information = models.TextField()
    payment_terms = models.CharField(
        max_length=10, choices=PaymentTerms.choices, default=PaymentTerms.NET_30
    )
    payment_method = models.CharField(
        max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.CREDIT_CARD
    )
    attachments = models.TextField()
    shipping_method = models.CharField(
        max_length=10, choices=ShippingMethod.choices, default=ShippingMethod.GROUND
    )
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    estimated_delivery_date = models.DateField()
    actual_delivery_date = models.DateField(null=True, blank=True)
    shipping_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.order_number
