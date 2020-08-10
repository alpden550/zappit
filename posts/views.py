from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from posts.models import Post, Vote
from posts.serializers import PostSerializer, VoteSerialiazer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class VoteCreateView(generics.CreateAPIView):
    serializer_class = VoteSerialiazer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post:)')
        post = Post.objects.get(pk=self.kwargs['pk'])
        serializer.save(voter=self.request.user, post=post)
