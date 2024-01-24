from django.urls import path
from songs.views import SongView

urlpatterns = [
    path("albums/<int:pk>/songs/", SongView.as_view()),
]
