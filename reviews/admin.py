from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    '''
    Admin panel for review posts
    '''
    list_display = ("title", "status", "created_on")
    search_fields = ["title", "content"]
    list_filter = ("status", "created_on")
    summernote_fields = ("content",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    '''
    Admin panel for comments on posts
    '''
    list_display = ("name", "body", "review", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        '''
        Function: for Admin to approved comments
        '''
        queryset.update(approved=True)
