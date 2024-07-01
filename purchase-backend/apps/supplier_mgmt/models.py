from uuid import uuid4
from django.contrib.postgres.fields import ArrayField
from django.db import models


class BaseAddress(models.Model):
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.city}, {self.state}, {self.country}"


class Address(BaseAddress):
    pass


class SocialLinks(models.Model):
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)


class BankDetails(models.Model):
    bank_name = models.CharField(max_length=255, blank=True)
    account_holder_name = models.CharField(max_length=255, blank=True)
    account_number = models.CharField(max_length=255, blank=True)


class ContactPerson(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.OneToOneField(
        Address,
        on_delete=models.CASCADE,
        related_name="contactaddress",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.first_name


class Supplier(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    company_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to="images/", blank=True)
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    address = models.ForeignKey(
        Address,
        on_delete=models.CASCADE,
        related_name="suppliers",
        blank=True,
        null=True,
    )
    social_links = models.OneToOneField(
        SocialLinks,
        on_delete=models.CASCADE,
        blank=True,
        related_name="supplierlinks",
        null=True,
    )
    contact_person_detail = models.OneToOneField(
        ContactPerson,
        on_delete=models.CASCADE,
        related_name="suppliercontact",
        blank=True,
        null=True,
    )
    phone = models.CharField(max_length=20, blank=True)
    bank_details = models.OneToOneField(
        BankDetails,
        on_delete=models.CASCADE,
        related_name="supplierbank",
        blank=True,
        null=True,
    )
    tax_id = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    rating = models.FloatField(null=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name
