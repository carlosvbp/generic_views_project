from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import UserSerializer
from users.permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = User.objects.all()
    serializer_class = UserSerializer
