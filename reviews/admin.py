from django.contrib import admin
from .models import Review, Comment
from django_summernote.admin import SummernoteModelAdmin

# was SummernoteModelAdmin
# summernote_fields = ("content",)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    '''
    Admin panel for review posts
    '''
    list_display = ('title', 'gamer', 'status', 'created_on', 'updated_on')
    search_fields = ['title', 'gamer', 'content']
    list_filter = ('status', 'gamer', 'created_on', 'updated_on')


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
