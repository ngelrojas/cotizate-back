from rest_framework import generics, authentication
from rest_framework import permissions, status, viewsets
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from user.serializers import UserSerializer, AuthTokenSerializer
from user.serializers import UserSerializerRetrieve
from user.serializers import ActivationAccountSerializer
from user.serializers import PasswordRecoverySerializer
from user.serializers import PasswordRecoveryConfirmSerializer
from core.models import CodeActivation, User, Biography
from core.tokens import decode_user_id


class CreateUserView(generics.CreateAPIView):
    """create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(viewsets.ModelViewSet):
    """manage the authenticated user"""
    serializer_class = UserSerializer
    serializer_class_re = UserSerializerRetrieve
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = User.objects.all()

    def retrieve(self, request, pk=None):
        queryset = User.objects.get(id=request.user.id)
        serializer = self.serializer_class_re(queryset)
        return Response(serializer.data)

    def partial_update(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class_re(
                request.user,
                data=request.data,
                partial=True
            )
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    {'data': 'current user updated'},
                    status=status.HTTP_200_OK
                )
        except User.DoesNotExist as err:
            return Response(
                {'error': f"{err}"},
                status=status.HTTP_404_NOT_FOUND
            )


class ActivationAccount(generics.UpdateAPIView):
    """
    update:
        update a current token to activate to current user
        and create profile current user.
    """
    serializer_class = ActivationAccountSerializer
    queryset = ''

    def update(self, request, *args, **kwargs):
        """
        update token
        """
        uid = self.kwargs.get('uid')
        token = self.kwargs.get('token')
        url_token = uid+'_'+token

        try:
            token = CodeActivation.objects.get(code_token=url_token)
        except CodeActivation.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if token.is_expired:
            return Response(
                    data={'detail': 'Expired Token'},
                    status=status.HTTP_400_BAD_REQUEST,
            )

        decode_url_id = decode_user_id(uid)

        user = get_object_or_404(User, id=decode_url_id)
        user.is_active = True
        user.save()

        token.is_expired = True
        token.save()

        self.create_biography_user(user)

        return Response(status=status.HTTP_200_OK)

    def create_biography_user(self, user):
        """create biography(profile user)"""
        return Biography.objects.create(user=user)


class PasswordRecovery(generics.CreateAPIView):
    """create and confirm password recovery"""
    serializer_class = PasswordRecoverySerializer
    render_classes = api_settings.DEFAULT_RENDERER_CLASSES


class PasswordRecoveryConfirm(generics.UpdateAPIView):
    serializer_class = PasswordRecoveryConfirmSerializer
    queryset = ''

    def put(self, request, *args):
        """recovery password done"""
        serializer = PasswordRecoveryConfirmSerializer(
                data=request.data,
                partial=True
        )
        if serializer.is_valid():
            user_id_uid = decode_user_id(request.data.get('uid'))
            current_user = get_object_or_404(User, id=user_id_uid)
            current_user.set_password(request.data.get('password'))
            current_user.save()
            return Response(
                    {'successfuly': 'Password recovery successfuly'}
            )
        return Response({'error': serializer.errors})


class PasswordUpdate(viewsets.ModelViewSet):
    serializer_class = PasswordRecoveryConfirmSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    queryset = ''

    def update(self, request, pk=None):

        password = request.data.get('password')
        password_confirm = request.data.get('password_confirm')

        if password != password_confirm:
            return Response(
                {'error': "Those passwords don't match."},
                status=status.HTTP_400_BAD_REQUEST
            )

        current_user = User.objects.get(id=request.user.id)
        current_user.set_password(request.data.get('password'))
        current_user.save()

        return Response(
            {'data': 'password updated.'},
            status=status.HTTP_200_OK
        )
