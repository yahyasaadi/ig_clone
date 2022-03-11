from django.urls import path
from .views import (PhotoListView,
                    PhotoCreateView,
                    PhotoDetailView,
                    PhotoUpdateView,
                    PhotoDeleteView,
                    UserPhotoListView,
                    LikeView,
                    CommentCreateView
)
from . import views

urlpatterns = [
    # path('home/', views.home, name='home-page')
    path('home/', PhotoListView.as_view(), name='home-page'),
    path('user/<str:username>', UserPhotoListView.as_view(), name='user-posts'),
    path('photo/<int:pk>/', PhotoDetailView.as_view(), name='photo-detail'),
    path('photo/new/', PhotoCreateView.as_view(), name='photo-create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('search/', views.search, name='search'),
    path('like/<int:pk>/', LikeView, name='like-photo'),
    # path('comment/<int:pk>/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<slug:username>/new', CommentCreateView.as_view(), name='comment-create'),
]