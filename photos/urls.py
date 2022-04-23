from django.urls import path
from .views import (
                    PhotoCreateView,
                    PhotoUpdateView,
                    PhotoDeleteView,
                    UserPhotoListView,
)
from . import views

urlpatterns = [
    path('', views.photos_list, name='home-page'),
    path('user/<str:username>', UserPhotoListView.as_view(), name='user-posts'),
    path('photo/<int:id>/', views.photo_details_view, name='photo-detail'),
    path('photo/new/', PhotoCreateView.as_view(), name='photo-create'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('search/', views.search, name='search'),
    path('comment/new/<int:id>/', views.add_comment, name='new-comment'),
    path('like/<int:id>', views.add_like, name='like')
]