from django.shortcuts import render, get_object_or_404
from .models import Testimony

def testimony_list(request):
    testimonies = Testimony.objects.all().order_by('-created_at')
    return render(request, 'testimonies/testimony_list.html', {'testimonies': testimonies})

def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'testimonies/testimony_detail.html', {'testimony': testimony})
