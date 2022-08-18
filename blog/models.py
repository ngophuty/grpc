
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100,primary_key=True,unique=False)
    # student = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']