# Generated by Django 4.2.14 on 2024-07-30 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_order_price_order_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=50, null=True),
        ),
    ]
