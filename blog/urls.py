from django.urls import path
from django.conf import settings

from . import views

from .views import IndexFirstListView, image_test_view, ArticleDetailViews
from django.conf.urls.static import static

urlpatterns = [
    #prova
    path("", IndexFirstListView.as_view(), name='home' ),
    path('image-test/', image_test_view, name='image_test'),
    path('arcticle/<slug:slug>/', ArticleDetailViews.as_view(), name='article_detail'),
    path('archive/<str:tag_name>/', views.archive_layout, name='archive_layout'),
    
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)