from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Biography
from biography.serializers import BiographySerializer
from biography.serializers import BiographyCompleteSerializer


class BiographyView(viewsets.ViewSet):
    """manage biography in the data base"""
    serializer_class = BiographySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        """retrieve biography to the current user"""
        try:
            current_user = Biography.objects.get(
                    user=request.user
            )
            return Response(
                    BiographySerializer(current_user).data,
                    status=status.HTTP_200_OK
            )
        except Biography.DoesNotExist as err:
            return Response(
                    {'error': f"{err}"},
                    status=status.HTTP_404_NOT_FOUND
            )

    def update(self, request, pk=None):
        """update biography to the current user"""
        try:
            current_user = Biography.objects.get(
                    user=request.user
            )
            serializer = BiographySerializer(
                    current_user,
                    data=request.data
            )

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        {'data': "biography updated sucessfuly"},
                        status=status.HTTP_200_OK
                )

        except Biography.DoesNotExist as err:
            return Response(
                    {'error': f"{err}"},
                    status=status.HTTP_400_BAD_REQUEST
            )


class BiographyComplete(viewsets.ViewSet):
    serializer_class = BiographyCompleteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None):
        queryset = Biography.objects.get(
                user=request.user
        )
        serializer = BiographyCompleteSerializer(queryset)
        return Response(serializer.data)
