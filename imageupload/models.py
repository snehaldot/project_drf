import uuid
from django.db import models
from PIL import Image
import os
from project import settings


# creates a thumbnail of an existing image
def create_thumbnail(input_image, thumbnail_size=(256, 256)):
    # make sure an image has been set
    if not input_image or input_image == "":
        return

    # open image
    image = Image.open(input_image)

    # use PILs thumbnail method; use anti aliasing to make the scaled picture look good
    image.thumbnail(thumbnail_size, Image.ANTIALIAS)

    # parse the filename and scramble it
    filename = scramble_uploaded_filename(None, os.path.basename(input_image.name))
    arrdata = filename.split(".")
    # extension is in the last element, pop it
    extension = arrdata.pop()
    basename = "".join(arrdata)
    # add _thumb to the filename
    new_filename = basename + "_thumb." + extension

    # save the image in MEDIA_ROOT and return the filename
    image.save(os.path.join(settings.MEDIA_ROOT, new_filename))

    return new_filename


def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)


# Our main model: Uploaded Image
class UploadedImage(models.Model):
    name = models.CharField(max_length=100, default=None, null=True)
    image = models.ImageField("Uploaded image", upload_to=scramble_uploaded_filename)
    thumbnail = models.ImageField("Thumbnail of uploaded image", blank=True)
    title = models.CharField("Title of the uploaded image", max_length=255, default="Unknown Picture")
    description = models.TextField("Description of the uploaded image", default="")

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):        
        self.thumbnail = create_thumbnail(self.image)
        super(UploadedImage, self).save()

    def __str__(self):
        return self.title
