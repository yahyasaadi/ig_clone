from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Photo, Comment, Like
from .forms import CommentForm


# Create your views here.
@login_required
def photos_list(request):
    photos = Photo.objects.all().order_by('-date_posted')
    context = {
        'photos': photos
    }
    return render(request, 'photos/photo_list.html', context)


class UserPhotoListView(ListView):
    model = Photo # blog/post_list.html requires this template to run
    template_name = 'photos/user_posts.html' # Or specify the template to use here
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Photo.objects.filter(owner=user).order_by('-date_posted')



class PhotoDetailView(DetailView):
    model = Photo

# Trying a function based view
def photo_detail(request):
    pass


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



# Comments view function
def add_comment(request, id):
    photo = get_object_or_404(Photo, id=id)
    # comments = Comment.objects.filter(image=photo)
    if request.method == 'POST':
        comment = request.POST['comment']
        new_comment = Comment(comment=comment, user=request.user, image=photo)

        comment_form = CommentForm(request.POST, instance=new_comment)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request, f'Your comment has been added!')
            return redirect('home-page')
    else:
        comment_form = CommentForm(instance=request.user)

    return render(request, 'photos/comment_form.html', context={'comment_form':comment_form})


def add_like(request, id):
    photo = get_object_or_404(Photo, id=id)
    like = Like.objects.filter(user=request.user, image=photo)

    if like:
        like.delete()
    else:
        new_like = Like(user=request.user, image=photo)
        new_like.save()
    return redirect('home-page')


# def LikeView(request, pk):
#     photo = get_object_or_404(Photo, id=request.POST.get('img_id'))
#     photo.like.add(request.user)
#     return HttpResponseRedirect(reverse('photo-detail', args=[str(pk)]))