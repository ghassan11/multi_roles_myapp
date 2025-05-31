from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

def home_view(request):
    return render(request, "base.html")

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # غيّر 'login' إذا كان اسم مسارك مختلف
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
