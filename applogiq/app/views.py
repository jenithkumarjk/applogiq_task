from django.shortcuts import render
from app.models import Patient,ErrorCharges 
from django.db.models import Count

def error_cards_view(request):
    error_charges_with_count = ErrorCharges.objects.annotate(patient_count=Count('patient_error_charge'))
    error_count = []
    for error_charges in error_charges_with_count:
        error_count.append({
            'error': error_charges.error,
            'description': error_charges.description,
            'patient_count': error_charges.patient_count
        })
    context = {
        'error_count':error_count
    }
    return render(request, 'dashboard.html', context)