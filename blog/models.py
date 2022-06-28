from django.db import models


class BlogPost(models.Model):
    """BlogPost model"""

    title = models.CharField(max_length=254)
    body = models.TextField()
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """posts in descending order"""
        ordering = ["-created"]

    def __str__(self):
        return self.title