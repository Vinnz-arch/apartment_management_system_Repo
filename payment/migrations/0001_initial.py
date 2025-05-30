# Generated by Django 4.2.8 on 2025-05-30 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lease', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('payment_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_method', models.CharField(choices=[('bank', 'Bank'), ('cash', 'Cash'), ('online', 'Online')], max_length=20)),
                ('receipt_number', models.CharField(max_length=100, unique=True)),
                ('lease', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='lease.lease')),
            ],
        ),
    ]
