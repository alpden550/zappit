from rest_framework import serializers

from posts.models import Post, Vote


class PostSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'title', 'url', 'created_at', 'user', 'user_id', 'votes')

    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()


class VoteSerialiazer(serializers.ModelSerializer):

    class Meta:
        model = Vote
        fields = ('id', )
