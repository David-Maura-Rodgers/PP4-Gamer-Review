from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Review(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    gamer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts"
    )
    game = models.TextField(default='placeholder')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='reviewpost_likes', blank=True)
    funny = models.ManyToManyField(
        User, related_name='reviewpost_funny', blank=True)
    insightful = models.ManyToManyField(
        User, related_name='reviewpost_insightful', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def number_of_funny(self):
        return self.funny.count()

    def number_of_insightful(self):
        return self.insightful.count()


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    c_likes = models.ManyToManyField(
        User, related_name='reviewpost_c_likes', blank=True)
    c_funny = models.ManyToManyField(
        User, related_name='reviewpost_c_funny', blank=True)
    c_insightful = models.ManyToManyField(
        User, related_name='reviewpost_c_insightful', blank=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def number_of_c_likes(self):
        return self.c_likes.count()

    def number_of_c_funny(self):
        return self.c_funny.count()

    def number_of_c_insightful(self):
        return self.c_insightful.count()