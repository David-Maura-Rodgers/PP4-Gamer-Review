from .models import Comment, Review
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ReviewForm(forms.ModelForm):
    '''
    Allows user to enter data in the fields below
    '''
    content = forms.CharField(widget=SummernoteWidget())

    class Meta:
        model = Review
        fields = ('title', 'game', 'subtitle', 'content',)
