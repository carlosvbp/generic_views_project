from django.urls import path
from albums import views

urlpatterns = [
    path("albums/", views.AlbumView.as_view()),
]
