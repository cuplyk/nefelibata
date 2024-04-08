from django.urls import path

from .views import IndexFirstListView, image_test_view

urlpatterns = [
    path("", IndexFirstListView.as_view(), name='home.html' ),
    path('image-test/', image_test_view, name='image_test'),
]