from django.shortcuts import render
from .models import Portfolio, PersonalInformation

def project_list(request):

    all_projects = Portfolio.objects.all()

    personal_info = PersonalInformation.objects.first()
    
    context = {
        'projects': all_projects,
        'personal_info': personal_info,
    }
    return render(request, 'home.html', context)

def project_detail(request, pk):
    single_project = Portfolio.objects.get(pk=pk)
    my_info = PersonalInformation.objects.first()
    
    context = {
        'project': single_project,
        'personal_info': my_info,
    }
    return render(request, 'portfolio/project_detail.html', context)