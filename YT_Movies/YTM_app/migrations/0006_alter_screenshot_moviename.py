# Generated by Django 4.1.7 on 2023-03-29 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YTM_app', '0005_actor_character_screenshot_remove_movie_cover_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screenshot',
            name='moviename',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Movie Name'),
        ),
    ]