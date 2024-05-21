from django.db.models.base import Model as Model
from django.shortcuts import render
from .models import Post, Tag
from django.shortcuts import get_list_or_404, get_object_or_404
from .utils import calculate_reading_time
from django.views.generic import TemplateView

from django.views.generic import TemplateView, DetailView
# Create your views here.


class IndexFirstListView(TemplateView):
    template_name = 'blog/blog_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the latest posts
        latest_posts = Post.objects.order_by('-created_on')[:4]
        
        # Calculate reading time for each post
        for post in latest_posts:
            post.reading_time = calculate_reading_time(post.content)

        context['posts'] = latest_posts  # Assign the calculated posts to the context

        # Fetch all tags
        tags = Tag.objects.all()
        context['tags'] = tags  # Assign tags to the context
        return context
    


class ArticleDetailViews(DetailView):
    model = Post
    template_name = 'blog/article_index.html'
    context_object_name = 'post'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(self.model, slug=slug)


def archive_layout(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/article_layout/article_author.html', {'posts': posts, 'tag': tag})







def image_test_view(request):
    posts = Post.objects.all()
    return render(request, 'image_test.html', {'posts': posts})