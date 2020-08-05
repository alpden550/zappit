from django.contrib import admin

from posts.models import Post, Vote


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    pass
