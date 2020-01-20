from rest_framework import serializers
from imageupload.models import UploadedImage # Import our UploadedImage model


class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        fields = ('pk', 'name', 'image', 'thumbnail', 'title', 'description',) # only serialize the primary key and the image field
        read_only_fields = ('thumbnail', )