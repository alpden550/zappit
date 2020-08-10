from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.serializers import PostSerializer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
