from rest_framework import serializers

from posts.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'created_at', 'user', 'user_id')


class VoteSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', )
