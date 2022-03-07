from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import Photo

# Create your views here.
def home(request):
    context = {
        'posts' : Photo.objects.all()
    }
    return render(request, 'photos/home.html')

class PhotoListView(ListView):
    model = Photo
    


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo 
    fields = ['img', 'caption']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)