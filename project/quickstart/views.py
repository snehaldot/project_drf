from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from project.quickstart.serializers import UserSerializer, GroupSerializer, ImageSerializer
from imageupload.serializers import UploadedImageSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from imageupload.models import UploadedImage
from django.core import serializers
import json
from django.http import Http404


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ImageViewSet(APIView):
    def get(self, request, format=None):
        image_list = UploadedImage.objects.all()
        serializer = UploadedImageSerializer(image_list, many=True)
        return Response(serializer.data)


class ImageDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get(self, request, pk):
        try:
            ret = UploadedImage.objects.get(pk=pk)
            serializer = UploadedImageSerializer(ret)
            return Response(serializer.data)
        except ImageDetail.DoesNotExist:
            raise Http404
