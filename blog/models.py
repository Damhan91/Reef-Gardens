from django.db import models


class Blog(models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
