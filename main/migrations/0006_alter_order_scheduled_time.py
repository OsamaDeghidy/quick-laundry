# Generated by Django 4.2.14 on 2024-07-23 11:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_order_scheduled_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='scheduled_time',
            field=models.TimeField(default=datetime.time(11, 35, 49, 639305)),
        ),
    ]
