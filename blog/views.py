from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

from django.views.generic import TemplateView
# Create your views here.


class IndexFirstListView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-created_on')[:4]
        return context
    
def image_test_view(request):
    posts = Post.objects.all()
    return render(request, 'image_test.html', {'posts': posts})