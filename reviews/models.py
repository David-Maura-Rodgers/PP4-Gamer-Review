from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

CONSOLE = (
    ('default', 'Please Select Console'),
    ('PS5', 'PS5'),
    ('PS4', 'PS4'),
    ('XBOX', 'XBOX'),
    ('NDS', 'NDS'),
    ('PC', 'PC'),
)


class Review(models.Model):
    """
    Model for user to create Game Reviews
    """
    title = models.CharField(max_length=100, blank=False)
    gamer = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    game = models.CharField(max_length=100, blank=False)
    subtitle = models.CharField(max_length=100, blank=True, default='')
    console = models.CharField(
        max_length=30, choices=CONSOLE, default='')
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name="reviewpost_likes", blank=True
    )
    funny = models.ManyToManyField(
        User, related_name="reviewpost_funny", blank=True
    )
    insightful = models.ManyToManyField(
        User, related_name="reviewpost_insightful", blank=True
    )

    class Meta:
        """
        Order review posts by dates they are created on
        """
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """
        Function: increases the number of likes count by one
        if user clicks on like icon in review detail page
        Also returns total number of likes
        """
        return self.likes.count()

    def number_of_funny(self):
        """
        Function: increases the number of funnny count by one
        if user clicks on like icon in review detail page
        Also returns total number of funny votes
        """
        return self.funny.count()

    def number_of_insightful(self):
        """
        Function: increases the number of insightful count by one
        if user clicks on like icon in review detail page
        Also returns total number of insightful votes
        """
        return self.insightful.count()


class Comment(models.Model):
    """
    Model for user to create comments for other Game Reviews
    """
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        """
        Order review posts by dates they are created on
        """
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
