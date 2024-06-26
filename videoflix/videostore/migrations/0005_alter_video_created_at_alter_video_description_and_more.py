# Generated by Django 5.0.6 on 2024-06-08 18:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videostore', '0004_alter_video_created_at_alter_video_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='video',
            name='description',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='video',
            name='hls_playlist',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='hls_playlist_files',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='original_video',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
    ]
