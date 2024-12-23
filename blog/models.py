from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class Post(models.Model):
    title = models.CharField()
    content = models.TextField()
    author = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title