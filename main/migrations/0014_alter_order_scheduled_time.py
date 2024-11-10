# Generated by Django 4.2.14 on 2024-08-17 08:34

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_order_payment_link_order_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='scheduled_time',
            field=models.TimeField(choices=[(datetime.time(6, 0), '6:00 AM'), (datetime.time(8, 0), '8:00 AM'), (datetime.time(10, 0), '10:00 AM'), (datetime.time(18, 0), '6:00 PM'), (datetime.time(20, 0), '8:00 PM')], default=django.utils.timezone.now),
        ),
    ]