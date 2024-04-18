from django.contrib import admin
from .models import Post, Tag, Comment
from django.db import models

from mdeditor.widgets import MDEditorWidget
from mdeditor.fields import MDTextField

from tinymce.widgets import TinyMCE



# Configurate the admin page



class TagAdmin(admin.ModelAdmin):
    pass

"""class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': MDEditorWidget}
    }

    raw_id_fields = ('author',)  # or autocomplete_fields = ('author',)
    filter_horizontal = ('tags',)  # or filter_vertical = ('tags',)
    

    list_display = ('title', 'author', 'created_on', 'status')  # Define fields to display in the list view
    list_filter = ('status', 'created_on')  # Add filters for status and created_on fields
    search_fields = ('title', 'content')  # Add search functionality for title and content fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug based on the title
"""

class CommentAdmin(admin.ModelAdmin):
    pass



class TinymcePostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})}
    }
    list_display = ('title', 'author', 'created_on', 'status')  # Define fields to display in the list view
    list_filter = ('status', 'created_on')  # Add filters for status and created_on fields
    search_fields = ('title', 'content')  # Add search functionality for title and content fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug based on the title



admin.site.register(Post, TinymcePostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)