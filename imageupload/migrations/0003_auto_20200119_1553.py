# Generated by Django 3.0.2 on 2020-01-19 15:53

from django.db import migrations, models
import imageupload.models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0002_uploadedimage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image',
            field=models.ImageField(upload_to=imageupload.models.scramble_uploaded_filename, verbose_name='Uploaded image'),
        ),
    ]
