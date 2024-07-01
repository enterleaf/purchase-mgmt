# choices.py

from django.db import models


class OrderStatus(models.TextChoices):
    DRAFT = "draft", "Draft"
    PENDING = "pending", "Pending"
    APPROVED = "approved", "Approved"
    REJECTED = "rejected", "Rejected"
    CANCELLED = "cancelled", "Cancelled"
    ON_HOLD = "on-hold", "On Hold"
    PROCESSING = "processing", "Processing"
    PARTIALLY_SHIPPED = "partially-shipped", "Partially Shipped"
    SHIPPED = "shipped", "Shipped"
    IN_TRANSIT = "in_transit", "In Transit"
    DELIVERED = "delivered", "Delivered"
    RECEIVED = "received", "Received"
    COMPLETED = "completed", "Completed"
    PARTIALLY_RECEIVED = "partially-received", "Partially Received"
    RETURNED = "returned", "Returned"
    REFUNDED = "refunded", "Refunded"
    CLOSED = "closed", "Closed"
    PAYMENT_RECEIVED = "payment-received", "Payment Received"
    AWAITING_PAYMENT = "awaiting-payment", "Awaiting Payment"


class PaymentTerms(models.TextChoices):
    NET_30 = "net 30", "Net 30"
    NET_60 = "net 60", "Net 60"


class PaymentMethod(models.TextChoices):
    CREDIT_CARD = "credit_card", "Credit Card"
    BANK_TRANSFER = "bank_transfer", "Bank Transfer"
    CASH = "cash", "Cash"


class ShippingMethod(models.TextChoices):
    GROUND = "ground", "Ground"
    AIR = "air", "Air"
    EXPRESS = "express", "Express"
