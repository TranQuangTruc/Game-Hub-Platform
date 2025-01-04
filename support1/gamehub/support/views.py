from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SupportRequestForm

def submit_support_request(request):
    if request.method == 'POST':
        form = SupportRequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your request has been submitted successfully!")
            return redirect('submit_support')
    else:
        form = SupportRequestForm()
    return render(request, 'support/submit_support.html', {'form': form})
