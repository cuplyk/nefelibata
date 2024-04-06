from django.urls import path

from .views import IndexFirstListView

urlpatterns = [
    path("", IndexFirstListView.as_view(), name='home.html' )
]