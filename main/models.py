from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime, time, timedelta

def get_default_date():
    return timezone.now().date()

def get_default_time():
    return time(6, 0)  # يمكنك تغيير الوقت الافتراضي هنا

TIME_CHOICES = [
    (time(6, 0), '6:00 AM'),
    (time(8, 0), '8:00 AM'),
    (time(10, 0), '10:00 AM'),
    (time(18, 0), '6:00 PM'),
    (time(20, 0), '8:00 PM'),
]

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_agent = models.ForeignKey('Users.DeliveryAgent', null=True, blank=True, on_delete=models.SET_NULL)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('claimed', 'Claimed'),
        ('completed', 'Completed'),
    ]

    order_date = models.DateTimeField(default=timezone.now)
    scheduled_date = models.DateField(default=get_default_date)
    scheduled_time = models.TimeField(choices=TIME_CHOICES, default=get_default_time,null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    weight = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True, default=0)
    price = models.DecimalField(max_digits=50, decimal_places=2, null=True, blank=True, default=0)
    payment_status = models.BooleanField(default=False)
    notes = models.TextField(null=True, blank=True)
    
    def get_scheduled_datetime(self):
        return timezone.make_aware(datetime.combine(self.scheduled_date, self.scheduled_time))

    def get_end_time(self):
        scheduled_datetime = self.get_scheduled_datetime()
        end_time = scheduled_datetime + timedelta(hours=8)
        return end_time
    
    def time_remaining(self):
        end_time = self.get_end_time()
        remaining_time = end_time - timezone.now()
        if remaining_time.total_seconds() < 0:
            return "0 hours, 0 minutes"
        remaining_seconds = int(remaining_time.total_seconds())
        hours, remainder = divmod(remaining_seconds, 3600)
        minutes, _ = divmod(remainder, 60)
        return f"{hours} hours, {minutes} minutes"


    def update_status(self):
        if self.status != 'claimed' and self.time_remaining() == "0 hours, 0 minutes":
            self.status = 'completed'
            self.save()

    def __str__(self):
        return f"Order {self.id} - {self.status}"
