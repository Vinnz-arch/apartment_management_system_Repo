from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import Tenant
from user.models import User, Role
from django.core.files.storage import FileSystemStorage


# Create your views here.


def tenants_registration(request):
    if request.method == 'POST':
        try:
            # Get or create the tenant role
            tenant_role, created = Role.objects.get_or_create(
                role_type='tenant',
                defaults={'role_type': 'tenant'}
            )
            if created:
                messages.info(request, 'Tenant role created successfully')
            
            # Create User instance
            user = User.objects.create(
                username=request.POST['username'],
                email=request.POST['email'],
                full_name=request.POST['full_name'],
                password=make_password(request.POST['password']),
                role=tenant_role
            )
            
            # Handle government ID file upload
            government_id = request.FILES.get('government_id')
            if government_id:
                fs = FileSystemStorage()
                filename = fs.save(f'government_ids/{government_id.name}', government_id)
                government_id_path = filename
            else:
                messages.error(request, 'Government ID is required')
                return redirect('tenants_registration')
            
            # Create Tenant instance
            tenant = Tenant.objects.create(
                user=user,
                phone_number=request.POST['phone_number'],
                government_id=government_id_path,
                date_of_birth=request.POST['date_of_birth'],
                occupation=request.POST['occupation'],
                employer_name=request.POST['employer_name'],
                emergency_contact_name=request.POST['emergency_contact_name'],
                emergency_contact_number=request.POST['emergency_contact_number'],
                address=request.POST['address']
            )
            
            messages.success(request, 'Tenant registered successfully!')
            return redirect('tenants_registration')
            
        except Exception as e:
            messages.error(request, f'Error registering tenant: {str(e)}')
            return redirect('tenants_registration')
    
    # Get all users with tenant role for display
    users = User.objects.filter(role__role_type='tenant')
    tenants = Tenant.objects.select_related('user').all()
    context = {
        'users': users,
        'tenants': tenants
    }
    return render(request, 'pages/registration/tenants_registration.html', context)


