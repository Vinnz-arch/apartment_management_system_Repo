from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tenants_registration(request):
    return render(request, 'pages/registration/tenants_registration.html')