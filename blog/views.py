from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_list_or_404

from django.views.generic import TemplateView, DeleteView
# Create your views here.


class IndexFirstListView(TemplateView):
    template_name = 'blog/blog_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_on')[:4]
        
        return context
    


class ArticleDetailViws(DeleteView):
    model = Post
    template_name = 'blog/articles/article_detail.html'
    context_object_name = 'article'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')

        return get_list_or_404(Post, slug=slug)






def image_test_view(request):
    posts = Post.objects.all()
    return render(request, 'image_test.html', {'posts': posts})