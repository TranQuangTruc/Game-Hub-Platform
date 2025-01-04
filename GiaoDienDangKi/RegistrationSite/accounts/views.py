from django.template import loader
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            template = loader.get_template('success')
            return redirect('success')
    else:
        form = RegistrationForm()
        template = loader.get_template('accounts/register.html')
    return render(request, 'accounts/register.html')