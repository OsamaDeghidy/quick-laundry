# Generated by Django 4.2.14 on 2024-07-23 11:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_order_scheduled_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='scheduled_date',
            field=models.DateField(default=datetime.date(2024, 7, 23)),
        ),
        migrations.AlterField(
            model_name='order',
            name='scheduled_time',
            field=models.TimeField(default=datetime.time(11, 36, 9, 428934)),
        ),
    ]