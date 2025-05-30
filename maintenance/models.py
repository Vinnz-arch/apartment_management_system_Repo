from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from apartment.models import ApartmentUnit

# Create your models here.

class MaintenanceRequest(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in-progress', 'In Progress'),
        ('closed', 'Closed'),
    ]

    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='maintenance_requests')
    apartment_unit = models.ForeignKey(ApartmentUnit, on_delete=models.CASCADE, related_name='maintenance_requests')
    description = models.TextField()
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')