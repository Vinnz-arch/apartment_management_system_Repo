from django.db import models
from user.models import User


# Create your models here.

class RentalAplication(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rental_applications')
    apartment_unit = models.ForeignKey('apartment.ApartmentUnit', on_delete=models.CASCADE, related_name='rental_applications')
    application_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')