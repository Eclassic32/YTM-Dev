# Generated by Django 4.1.7 on 2023-03-27 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genreName', models.CharField(blank=True, max_length=50, null=True, verbose_name='Genre')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Movie name')),
                ('year', models.IntegerField(blank=True, null=True, verbose_name='Year')),
                ('producer', models.CharField(blank=True, max_length=255, null=True, verbose_name='Producer')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('cover', models.CharField(blank=True, max_length=500, null=True, verbose_name='Cover URL')),
                ('poster', models.CharField(blank=True, max_length=500, null=True, verbose_name='Poster URL')),
                ('movieLink', models.CharField(blank=True, max_length=500, null=True, verbose_name='Movie URL')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='YTM_app.genre', verbose_name='Genre')),
            ],
        ),
    ]