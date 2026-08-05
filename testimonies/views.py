from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from .models import Testimony
from .forms import TestimonyForm

class TestimonyListView(ListView):
    model = Testimony
    template_name = 'testimonies/testimony_list.html'
    context_object_name = 'testimonies'
    ordering = ['-created_at']

def testimony_detail(request, pk):
    testimony = get_object_or_404(Testimony, pk=pk)
    return render(request, 'testimonies/testimony_detail.html', {'testimony': testimony})

def testimony_create_view(request):
    if request.method == 'POST':
        form = TestimonyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimony_list')
    else:
        form = TestimonyForm()
    return render(request, 'testimonies/create.html', {'form': form})
