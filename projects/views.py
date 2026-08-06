from django.shortcuts import render, get_object_or_404, redirect
from .models import Project
from .forms import ProjectForm

def project_list_view(request):
    projects = Project.objects.all()
    return render(request, 'projects/list.html', {'projects': projects})

def project_detail_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'projects/detail.html', {'project': project})

def project_create_view(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/create.html', {'form': form})