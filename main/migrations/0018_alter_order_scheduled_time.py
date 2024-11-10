# Generated by Django 4.2.14 on 2024-11-09 18:23

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_alter_order_scheduled_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='scheduled_time',
            field=models.TimeField(blank=True, choices=[('6:00 AM', '6:00 AM'), ('8:00 AM', '8:00 AM'), ('10:00 AM', '10:00 AM'), ('6:00 PM', '6:00 PM'), ('8:00 PM', '8:00 PM')], default=main.models.get_default_time, null=True),
        ),
    ]