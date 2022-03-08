from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Photo

# Create your views here.
def home(request):
    context = {
        'posts' : Photo.objects.all()
    }
    return render(request, 'photos/home.html')

class PhotoListView(ListView):
    model = Photo
    ordering = ['-date_posted']
    

class PhotoDetailView(DetailView):
    model = Photo


class PhotoCreateView(LoginRequiredMixin, CreateView):
    model = Photo 
    fields = ['img', 'caption']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class PhotoUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Photo 
    fields = ['img', 'caption']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.owner:
            return True
        return False


class PhotoDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Photo
    success_url = '/home'

    def test_func(self):
        photo = self.get_object()
        if self.request.user == photo.owner:
            return True
        return False