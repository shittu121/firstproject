# Generated by Django 4.2.3 on 2023-09-20 04:48

from django.db import migrations, models
import firstapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=firstapp.models.get_file_path)),
            ],
        ),
    ]