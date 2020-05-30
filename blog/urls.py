from django.urls import path
from .views import PostListView
from . import views


urlpatterns=[
    path('',views.PostListView.as_view(), name="blog-home"),
    path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),
]