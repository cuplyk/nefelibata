from django.contrib import admin
from .models import Post, Tag, Comment
from django.db import models

from mdeditor.widgets import MDEditorWidget



# Configurate the admin page



class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }
    list_display = ('title', 'author', 'created_on', 'status')  # Define fields to display in the list view
    list_filter = ('status', 'created_on')  # Add filters for status and created_on fields
    search_fields = ('title', 'content')  # Add search functionality for title and content fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug based on the title


class CommentAdmin(admin.ModelAdmin):
    pass




admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)