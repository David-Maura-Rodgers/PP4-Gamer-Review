from .models import Comment, Review
from django import forms


class CommentForm(forms.ModelForm):
    '''
    Users can leave comments
    '''
    class Meta:
        '''
        Model and fields needed for comments
        '''
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    '''
    Users can post a review
    '''
    class Meta:
        '''
        Model and fields needed for reviews
        '''
        model = Review
        fields = ('title', 'game', 'subtitle', 'content',)
