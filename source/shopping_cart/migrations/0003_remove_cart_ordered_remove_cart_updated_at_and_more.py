# Generated by Django 5.1.7 on 2025-03-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_cart', '0002_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='ordered_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
