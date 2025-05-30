from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
from .models import ApartmentUnit

# Create your views here.

def unit_info(request):
    if request.method == 'POST':
        unit_id = request.POST.get('unit_id')
        if request.POST.get('delete_unit_id'):
            # Handle delete operation
            unit = get_object_or_404(ApartmentUnit, id=request.POST.get('delete_unit_id'))
            unit.delete()
            messages.success(request, 'Unit deleted successfully.')
            return redirect('apartment_unit:unit_info')
        
        # Handle create/update operation
        data = {
            'unit_number': request.POST.get('unit_number'),
            'floor_number': request.POST.get('floor_number'),
            'bedrooms': request.POST.get('bedrooms'),
            'bathrooms': request.POST.get('bathrooms'),
            'monthly_rent': request.POST.get('monthly_rent'),
            'status': request.POST.get('status'),
        }
        
        try:
            if unit_id:
                # Update existing unit
                unit = get_object_or_404(ApartmentUnit, id=unit_id)
                for key, value in data.items():
                    setattr(unit, key, value)
                unit.save()
                messages.success(request, 'Unit updated successfully.')
            else:
                # Create new unit
                ApartmentUnit.objects.create(**data)
                messages.success(request, 'Unit created successfully.')
        except Exception as e:
            messages.error(request, f'Error: {str(e)}')
        
        return redirect('apartment_unit:unit_info')
    
    # GET request - display units
    search_query = request.GET.get('search', '')
    units = ApartmentUnit.objects.all()
    
    if search_query:
        units = units.filter(unit_number__icontains=search_query)
    
    return render(request, 'pages/unitInfo/unit_info.html', {'units': units})

def get_unit_details(request, unit_id):
    """API endpoint to get unit details for editing"""
    unit = get_object_or_404(ApartmentUnit, id=unit_id)
    data = {
        'id': unit.id,
        'unit_number': unit.unit_number,
        'floor_number': unit.floor_number,
        'bedrooms': unit.bedrooms,
        'bathrooms': unit.bathrooms,
        'monthly_rent': str(unit.monthly_rent),
        'status': unit.status,
    }
    return JsonResponse(data)