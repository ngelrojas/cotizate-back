from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Raised
from raised.serializers import RaisedSerializer


class RaisedPrivate(viewsets.ModelViewSet):
    """
    create:
        create a raised
    """
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Raised.objects.all()
    serializer_class = RaisedSerializer

    def perform_create(self, serializer):
        return serializer.save()

    def update(self, request, pk):
        curernt_raised = Raised.objects.get(id=pk)
        serializer = self.serializer_class(
                curernt_raised,
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
