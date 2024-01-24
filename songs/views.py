from rest_framework.generics import ListCreateAPIView
from albums.models import Album
from .models import Song
from .serializers import SongSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.shortcuts import get_object_or_404


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs.get("pk"))

        serializer.save(album=album)
