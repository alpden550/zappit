from rest_framework import generics

from posts.models import Post
from posts.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
