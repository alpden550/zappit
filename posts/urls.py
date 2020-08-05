from django.urls import path

from posts import views

app_name = 'posts'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts-list'),
]
