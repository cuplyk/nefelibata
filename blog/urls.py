from django.urls import path
from django.conf import settings

from .views import IndexFirstListView, image_test_view, ArticleDetailViws
from django.conf.urls.static import static

urlpatterns = [
    #prova
    path("", IndexFirstListView.as_view(), name='home.html' ),
    path('image-test/', image_test_view, name='image_test'),
    path('arcticle/<slug:slug>/', ArticleDetailViws.as_view(), name='article_detail')
    
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)