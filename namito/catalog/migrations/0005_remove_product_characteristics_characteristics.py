# Generated by Django 4.2.11 on 2024-04-19 05:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_characteristics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='characteristics',
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=255, null=True, verbose_name='Key')),
                ('value', models.CharField(blank=True, max_length=255, null=True, verbose_name='Value')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
        ),
    ]
