# Generated by Django 4.2.3 on 2023-09-20 12:17

from django.db import migrations, models
import firstapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0009_remove_slider_image_slider_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=firstapp.models.get_file_path),
        ),
    ]