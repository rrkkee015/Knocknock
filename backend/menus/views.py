from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from menus.models import Menu
from menus.serializers import MenuSerializer


class CreateMenuAPI(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        body = {'message': '메뉴 등록 완료', 'body': serializer.data}
        return Response(body, status=status.HTTP_201_CREATED)


class RetrieveUpdateDestroyMenuAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MenuSerializer

    def get_object(self):
        obj = get_object_or_404(Menu, pk=self.kwargs.get('menu_id'))
        return obj
