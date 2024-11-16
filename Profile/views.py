from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_user(request):
    data = UserModel.objects.all()
    return Response(UserSerializers(data, many=True).data, status=status.HTTP_200_OK)
