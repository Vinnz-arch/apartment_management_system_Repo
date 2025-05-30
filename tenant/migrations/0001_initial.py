# Generated by Django 4.2.8 on 2025-05-27 23:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('government_id', models.ImageField(help_text='National ID/Passport', max_length=50, upload_to='')),
                ('date_of_birth', models.DateField()),
                ('occupation', models.CharField(max_length=100)),
                ('employer_name', models.CharField(max_length=255)),
                ('emergency_contact_name', models.CharField(max_length=255)),
                ('emergency_contact_number', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenant_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbl_tenants',
            },
        ),
    ]
