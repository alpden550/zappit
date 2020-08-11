from rest_framework import generics, mixins, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response

from posts.models import Post, Vote
from posts.serializers import PostSerializer, VoteSerialiazer


class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostRetieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def delete(self, request, *args, **kwargs):
        post = Post.objects.filter(user=request.user, pk=kwargs['pk'])
        if not post.exists():
            raise ValidationError("This isn't your post to delete.")

        return self.destroy(request, *args, **kwargs)


class VoteCreateView(generics.CreateAPIView, mixins.DestroyModelMixin):
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

    def delete(self, request, *args, **kwargs):
        if not self.get_queryset().exists():
            raise ValidationError('You never voted for this post.')

        self.get_queryset().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
