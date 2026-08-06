from django.shortcuts import render, redirect
from .forms import InquiryForm

def inquiry_create_view(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_success')  # we’ll define this URL later
    else:
        form = InquiryForm()
    return render(request, 'contact.html', {'form': form})