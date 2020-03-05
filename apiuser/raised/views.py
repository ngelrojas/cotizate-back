from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Raised
from raised.serializers import RaisedSerializer


class RaisedPrivate(viewsets.ModelViewSet):
    """
    retrieve:
        get a raised details
    create:
        create a raised
    update:
        update a current raised
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Raised.objects.all()
    serializer_class = RaisedSerializer

    def retrieve(self, request, pk):
        try:
            current_raised = Raised.objects.get(campaing=pk)
            serializer = self.serializer_class(
                        current_raised,
                        data=request.data
            )
            if serializer.is_valid(raise_exception=True):
                return Response(
                        {'data': serializer.data},
                        status=status.HTTP_200_OK
                )
            return Response(
                    status=status.HTTP_404_NOT_FOUND
            )
        except Raised.DoesNotExist as err:
            return Response(
                    {'error': f'{err}'},
                    status=status.HTTP_400_BAD_REQUEST
            )

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, pk=None):
        try:
            raised_id = request.data.get('raised_id')
            current_raised = Raised.objects.get(id=raised_id)
            serializer = self.serializer_class(
                    current_raised,
                    data=request.data,
                    partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': serializer.data},
                        status=status.HTTP_200_OK
                )
            return Response(
                    {'error': 'error'},
                    status=status.HTTP_400_BAD_REQUEST
            )
        except Raised.DoesNotExist as err:
            return Response(
                    status=status.HTTP_400_BAD_REQUEST
            )


class RaisedPublic(viewsets.ModelViewSet):
    """
    retrieve:
        get a detail public raised
    """
    # queryset = Raised.objects.all()
    serializer_class = RaisedSerializer

    def retrieve(self, request, pk):
        try:
            queryset_raised = Raised.objects.get(id=pk)
            serializer = self.serializer_class(
                    queryset_raised,
                    data=request.data
            )
            if serializer.is_valid(raise_exception=True):
                return Response(
                        {'data': serializer.data},
                        status=status.HTTP_200_OK
                )
            return Response(
                    {'error': 'error'},
                    status=status.HTTP_400_BAD_REQUEST
            )
        except Raised.DoesNotExist as err:
            return Response(
                    status=status.HTTP_404_NOT_FOUND
            )
