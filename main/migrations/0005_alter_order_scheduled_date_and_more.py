# Generated by Django 4.2.14 on 2024-07-23 11:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_order_scheduled_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='scheduled_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='scheduled_time',
            field=models.TimeField(default=datetime.time(11, 34, 24, 832055)),
        ),
    ]
