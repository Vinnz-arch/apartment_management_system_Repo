from django.db import models
from user.models import User

class Tenant(models.Model):
    class Meta:
        db_table = 'tbl_tenants'


    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tenant_profile')
    phone_number = models.CharField(max_length=20, blank=False, unique=True)
    government_id = models.ImageField(max_length=50, blank=False, help_text='National ID/Passport')
    date_of_birth = models.DateField(blank=False)
    occupation = models.CharField(max_length=100, blank=False)
    employer_name = models.CharField(max_length=255, blank=False)
    emergency_contact_name = models.CharField(max_length=255, blank=False)
    emergency_contact_number = models.CharField(max_length=20, blank=False)
    address = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

