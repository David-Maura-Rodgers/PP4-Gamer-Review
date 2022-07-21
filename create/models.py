from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class GamerReview(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    gamer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="create_review"
    )
    game = models.TextField(default='placeholder')
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

