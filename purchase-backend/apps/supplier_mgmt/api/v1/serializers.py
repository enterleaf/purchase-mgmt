from rest_framework import serializers
from apps.supplier_mgmt.models import (
    Address,
    SocialLinks,
    BankDetails,
    ContactPerson,
    Supplier,
)


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["city", "state", "country"]


class SocialLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLinks
        fields = ["facebook", "instagram", "twitter", "linkedin"]


class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = ["bank_name", "account_holder_name", "account_number"]


class ContactPersonSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)

    class Meta:
        model = ContactPerson
        fields = ["first_name", "last_name", "phone", "email", "address"]

    def create(self, validated_data):
        address_data = validated_data.pop("address", None)
        address_instance = (
            Address.objects.create(**address_data) if address_data else None
        )
        validated_data["address"] = address_instance
        return super().create(validated_data)

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)
        if address_data:
            Address.objects.update_or_create(
                defaults=address_data, id=instance.address_id
            )
        return super().update(instance, validated_data)


class SupplierSerializer(serializers.ModelSerializer):
    address = AddressSerializer(required=False)
    social_links = SocialLinksSerializer(required=False)
    contact_person_detail = ContactPersonSerializer(required=False)
    bank_details = BankDetailsSerializer(required=False)

    class Meta:
        model = Supplier
        fields = [
            "uuid",
            "company_name",
            "avatar",
            "total_amount",
            "address",
            "social_links",
            "contact_person_detail",
            "bank_details",
            "phone",
            "tax_id",
            "email",
            "rating",
            "description",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        address_data = validated_data.pop("address", None)
        social_links_data = validated_data.pop("social_links", None)
        contact_person_data = validated_data.pop("contact_person_detail", None)
        bank_details_data = validated_data.pop("bank_details", None)

        # Create or get address instance if data is provided
        address_instance = None
        if address_data:
            address_instance, _ = Address.objects.get_or_create(**address_data)

        # Create social links instance if data is provided
        social_links_instance = None
        if social_links_data:
            social_links_instance, _ = SocialLinks.objects.get_or_create(
                **social_links_data
            )

        # Create contact person instance if data is provided
        contact_person_instance = None
        if contact_person_data:
            contact_person_address_data = contact_person_data.pop("address", None)
            contact_person_address_instance = None
            if contact_person_address_data:
                contact_person_address_instance, _ = Address.objects.get_or_create(
                    **contact_person_address_data
                )

            # Check for other fields  than address in contact_person_data
            if any(contact_person_data.values()) or contact_person_address_instance:
                contact_person_instance, _ = ContactPerson.objects.get_or_create(
                    address=contact_person_address_instance, **contact_person_data
                )

        # Create bank details instance if data is provided
        bank_details_instance = None
        if bank_details_data:
            bank_details_instance, _ = BankDetails.objects.get_or_create(
                **bank_details_data
            )

        # Create the supplier instance with all related instances
        supplier_instance = Supplier.objects.create(
            address=address_instance,
            social_links=social_links_instance,
            contact_person_detail=contact_person_instance,
            bank_details=bank_details_instance,
            **validated_data
        )

        return supplier_instance

    def update(self, instance, validated_data):
        address_data = validated_data.pop("address", None)
        social_links_data = validated_data.pop("social_links", None)
        contact_person_data = validated_data.pop("contact_person_detail", None)
        bank_details_data = validated_data.pop("bank_details", None)

        if address_data:
            Address.objects.update_or_create(
                defaults=address_data, id=instance.address_id
            )
        if social_links_data:
            SocialLinks.objects.update_or_create(
                defaults=social_links_data, id=instance.social_links_id
            )
        if contact_person_data:
            contact_person_address_data = contact_person_data.pop("address", None)
            if contact_person_address_data:
                Address.objects.update_or_create(
                    defaults=contact_person_address_data,
                    id=instance.contact_person_detail.address_id,
                )
            ContactPerson.objects.update_or_create(
                defaults=contact_person_data, id=instance.contact_person_detail_id
            )
        if bank_details_data:
            BankDetails.objects.update_or_create(
                defaults=bank_details_data, id=instance.bank_details_id
            )

        return super().update(instance, validated_data)
