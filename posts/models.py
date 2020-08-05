from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=150)
    url = models.URLField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        get_user_model(),
        verbose_name='User',
        on_delete=models.CASCADE,
        related_name='posts',
    )

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
