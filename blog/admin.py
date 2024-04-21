from django.contrib import admin
from .models import Post, Tag, Comment
from django.db import models
from django.urls import reverse


from tinymce.widgets import TinyMCE



class TagAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass



class TinymcePostAdmin(admin.ModelAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce-linklist')},
            ))
        return super().formfield_for_dbfield(db_field, **kwargs)

    list_display = ('title', 'author', 'created_on', 'status')  # Define fields to display in the list view
    list_filter = ('status', 'created_on')  # Add filters for status and created_on fields
    search_fields = ('title', 'content')  # Add search functionality for title and content fields
    prepopulated_fields = {'slug': ('title',)}  # Automatically generate slug based on the title



admin.site.register(Post, TinymcePostAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment, CommentAdmin)