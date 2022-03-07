from django.shortcuts import render
from django.views.generic import ListView
from .models import Photo

# Create your views here.
def home(request):
    context = {
        'posts' : Photo.objects.all()
    }
    return render(request, 'photos/home.html')

def PhotoListView(ListView):
    model = Photo
    