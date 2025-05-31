from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'registration/register_done.html')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})