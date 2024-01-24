from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from users.permissions import IsAccountOwner
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404


class ListModelMixin(PageNumberPagination):
    queryset = None
    serializer_class = None

    def list(self, request: Request):
        queryset = self.queryset.all()
        return Response(
            self.get_paginated_response(self.serializer_class(queryset, many=True).data)
        )


class CreateModelMixin:
    serializer_class = None

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class RetrieveModelMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = None
    serializer_class = None

    def retrieve(self, request: Request, pk) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        self.check_object_permissions(request, instance)
        return Response(self.serializer_class(instance).data)


class UpdateModelMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = None
    serializer_class = None

    def partial_update(self, request: Request, pk) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        self.check_object_permissions(request, instance)
        serializer = self.serializer_class(instance, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class DestroyModelMixin:
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = None

    def destroy(self, request: Request, pk) -> Response:
        instance = get_object_or_404(self.queryset.all(), pk=pk)
        self.check_object_permissions(request, instance)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
