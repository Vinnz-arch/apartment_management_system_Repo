from django.db import models
from lease.models import Lease

# Create your models here.

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('bank', 'Bank'),
        ('cash', 'Cash'),
        ('online', 'Online'),
    ]

    id = models.BigAutoField(primary_key=True)
    lease = models.ForeignKey(Lease, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    receipt_number = models.CharField(max_length=100, unique=True)