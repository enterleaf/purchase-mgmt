from rest_framework import serializers
from apps.order_mgmt.models import Order
from apps.supplier_mgmt.models import Supplier, Address


class OrderSerializer(serializers.ModelSerializer):
    supplier = serializers.SlugRelatedField(
        queryset=Supplier.objects.all(), slug_field="company_name"
    )
    shipping_address = serializers.SlugRelatedField(
        queryset=Address.objects.all(), slug_field="city"
    )

    class Meta:
        model = Order
        fields = [
            "order_number",
            "order_date",
            "supplier",
            "order_status",
            "supplier_name",
            "product_id",
            "product_name",
            "quantity_ordered",
            "unit_price",
            "total_price",
            "product_category",
            "discount",
            "tax",
            "created_at",
            "updated_at",
            "payment_information",
            "payment_terms",
            "payment_method",
            "attachments",
            "shipping_method",
            "shipping_cost",
            "estimated_delivery_date",
            "actual_delivery_date",
            "shipping_address",
            "country",
            "state",
            "city",
        ]

    def create(self, validated_data):
        quantity_ordered = validated_data.get("quantity_ordered")
        unit_price = validated_data.get("unit_price")

        total_price = quantity_ordered * unit_price
        validated_data["total_price"] = total_price

        return super().create(validated_data)
