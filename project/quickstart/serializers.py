from django.contrib.auth.models import User, Group
from imageupload.models import UploadedImage
# from project.quickstart.models import Photo
from rest_framework import serializers
# from project.quickstart.models import *


# import ipdb; ipdb.set_trace()
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ImageSerializer(serializers.Serializer):
    image = serializers.ImageField


class ImagesSerializer(serializers.Serializer):
    images = ImageSerializer(many=True)


    # content = serializers.CharField(max_length=200)
    # created = serializers.DateTimeField()


# class ImageSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = UploadedImage
#         fields = ['image']


# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = "__all__"
