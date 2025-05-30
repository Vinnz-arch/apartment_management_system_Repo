from django.db import models

# Create your models here.

class ApartmentUnit(models.Model):
    id = models.BigAutoField(primary_key=True)
    unit_number = models.CharField(max_length=20, unique=True, blank=False)
    floor_number = models.IntegerField(blank=False)
    bedrooms = models.IntegerField(blank=False)
    bathrooms = models.IntegerField(blank=False)
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available',  blank=False)
    created_at = models.DateTimeField(auto_now_add=True)