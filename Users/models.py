from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
   
    phone_number = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],
        verbose_name="Phone Number"
    )
    house_number = models.CharField(max_length=10, verbose_name="Apartment/House Number")
    street_name = models.CharField(max_length=100, verbose_name="Street Name")
    street_number = models.CharField(max_length=10, verbose_name="Street Number")
    postal_code = models.CharField(max_length=10, verbose_name="Postal Code")
    area = models.CharField(max_length=100, verbose_name="Area")

    def __str__(self):
        return f"{self.user} - {self.phone_number}"

class DeliveryAgent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, verbose_name="Phone Number")
    address = models.CharField(max_length=255, verbose_name="Address")
    is_approved = models.BooleanField(default=False, verbose_name="Is Approved")

    def __str__(self):
        return self.user.username
