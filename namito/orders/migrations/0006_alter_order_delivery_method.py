# Generated by Django 4.2.11 on 2024-04-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_order_delivery_address_order_user_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_method',
            field=models.CharField(choices=[('курьером', 'Курьером'), ('самовывоз', 'Самовывоз')], default='курьером', max_length=20),
        ),
    ]
