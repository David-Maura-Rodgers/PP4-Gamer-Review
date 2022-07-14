from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)

