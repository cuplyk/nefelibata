from django.urls import path
from django.conf import settings

from .views import IndexFirstListView, image_test_view
from django.conf.urls.static import static

urlpatterns = [
    path("", IndexFirstListView.as_view(), name='home.html' ),
    path('image-test/', image_test_view, name='image_test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)