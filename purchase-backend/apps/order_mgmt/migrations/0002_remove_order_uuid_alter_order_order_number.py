# Generated by Django 5.0.6 on 2024-06-30 10:09

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_mgmt', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
