from django.shortcuts import render
from .models import Testimony

def testimony_list(request):
    testimonies = Testimony.objects.all().order_by('-created_at')
    return render(request, 'testimonies/testimony_list.html', {'testimonies': testimonies})
