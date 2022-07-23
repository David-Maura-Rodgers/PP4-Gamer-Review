from .models import Comment, Review
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'game', 'subtitle', 'content',)
