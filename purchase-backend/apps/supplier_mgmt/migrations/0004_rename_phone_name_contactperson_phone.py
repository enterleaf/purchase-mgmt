# Generated by Django 5.0.6 on 2024-06-30 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supplier_mgmt', '0003_alter_supplier_address_alter_supplier_bank_details_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactperson',
            old_name='phone_name',
            new_name='phone',
        ),
    ]
