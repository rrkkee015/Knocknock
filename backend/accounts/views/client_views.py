from django.shortcuts import get_object_or_404
from django.contrib.auth.signals import user_logged_out
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from accounts.models import Client
from accounts.serializers.client_serializers import (
    ClientSignupSerializer,
    LoginSerializer,
    UserSerializer,
    ClientSerializer,
)
from knox.models import AuthToken


class ClientSignupAPI(generics.GenericAPIView):
    serializer_class = ClientSignupSerializer

    def post(self, request, *args, **kwargs):
        if len(request.data['username']) < 6:       # 아이디 유효성 검사
            body = {'message': '아이디는 6자 이상으로'}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        if len(request.data['password']) < 6:       # 비밀번호 유효성 검사
            body = {'message': '비밀번호는 6자 이상으로'}   
            return Response(body, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '회원가입 완료'}
        return Response(body, status=status.HTTP_201_CREATED)


class ClientLoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        client = get_object_or_404(Client, user=user)
        return Response(
            {
                "profile": ClientSerializer(client, context=self.get_serializer_context()).data,
                "user": {
                    "username": user.username,
                    "token": AuthToken.objects.create(user)[1],
                }
            },
            status = status.HTTP_202_ACCEPTED
        )


class ClientUserAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        client = Client.objects.get(user=self.request.user)
        return Response(
            {
                'profile': ClientSerializer(client, context=self.get_serializer_context()).data,
                'username': client.user.username
            },
            status = status.HTTP_202_ACCEPTED
        )


class ClientLogoutAPI(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        return Response({'message': '로그아웃 완료'}, status=status.HTTP_202_ACCEPTED)