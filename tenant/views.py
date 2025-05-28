from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.

def tenants_registration(request):
    return render(request, 'pages/registration/tenants_registration.html')