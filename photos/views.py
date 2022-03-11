from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Photo, Comment, Like

# Create your views here.
def home(request):
    context = {
        'posts' : Photo.objects.all()
    }
    return render(request, 'photos/home.html')

class PhotoListView(ListView):
    model = Photo
    ordering = ['-date_posted']
    

class UserPhotoListView(ListView):
    model = Photo # blog/post_list.html requires this template to run
    template_name = 'blog/user_posts.html' # Or specify the template to use here
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Photo.objects.filter(owner=user).order_by('-date_posted')



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



# Search method
def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		pics = Photo.objects.filter(owner__username__contains=searched)
	
		return render(request, 'photos/search.html', {'pics':pics})
	else:
		return render(request, 'photos/search.html')




# Comments Views
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment 
    fields = ['comment']

    def form_valid(self, form):
        photo = self.get_object()
        form.instance.photo = photo
        form.instance.owner = self.request.user
        # form.save()
        return super().form_valid(form)


def LikeView(request, pk):
    photo = get_object_or_404(Photo, id=request.POST.get('img_id'))
    photo.like.add(request.user)
    return HttpResponseRedirect(reverse('photo-detail', args=[str(pk)]))