from django.shortcuts import render
from . import models

# Create your views here.
def list_patient(request):
    
    all_patients = models.Patient.objects.all()
    context = {'patients':all_patients}

    return render(request, 'office/list.html', context=context)

