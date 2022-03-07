from django.urls import path
from .views import PhotoListView, PhotoCreateView
from . import views

urlpatterns = [
    # path('home/', views.home, name='home-page')
    path('home/', PhotoListView.as_view(), name='home-page'),
    path('post/new/', PhotoCreateView.as_view(), name='photo-create')
]