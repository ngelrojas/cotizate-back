from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import CategoryCampaing
from category import serializers


class CategoryViewSet(
        viewsets.GenericViewSet,
        mixins.ListModelMixin,
        mixins.CreateModelMixin,
        mixins.DestroyModelMixin):
    """
    list:
        show all categories
    retrieve:
        show a category
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = CategoryCampaing.objects.all()
    serializer_class = serializers.CategoryCampaingSerializer

    def get_queryset(self):
        return self.queryset.all().order_by('-name')

    def retrieve(self, request, pk):
        queryset = CategoryCampaing.objects.all()
        current_category = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(current_category)
        return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
        )


class CategoryPublic(
        viewsets.GenericViewSet,
        mixins.ListModelMixin):
    """
    list:
        display all categories
    retrieve:
        display detail category
    """
    serializer_class = serializers.CategoryPublicSerializer
    queryset = CategoryCampaing.objects.all()

    def get_queryset(self):
        return self.queryset.order_by('-name')

    def retrieve(self, request, name):
        current_cc = get_object_or_404(self.queryset, name=name)
        serializer = self.serializer_class(current_cc)
        return Response(
                {'data': serializer.data},
                status=status.HTTP_200_OK
        )


class CategoryPublicGeneral(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
        class category public general
    """
    serializer_class = serializers.CategoryPublicGeneral
    queryset = CategoryCampaing.objects.all()

    def get_queryset(self):
        """list all categories public"""
        return self.queryset.order_by('name')
