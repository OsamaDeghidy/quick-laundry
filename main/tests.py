from django.test import TestCase

# Create your tests here.
# tasks.py
from celery import shared_task
from .models import Order

@shared_task
def update_order_status():
    orders = Order.objects.filter(status='pending')
    for order in orders:
        order.update_status()
