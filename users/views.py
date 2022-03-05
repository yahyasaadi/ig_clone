from django.shortcuts import render, redirect
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})