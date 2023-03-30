from django.db import models
from pytils.translit import slugify

# Create your models here.

class Genre (models.Model):
    genreName = models.CharField("Genre", max_length=50, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return self.genreName
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.genreName)
        super().save(*args, **kwargs)

class Actor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Character(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    movieName = models.CharField("Movie name", max_length=255, null=True, blank=True)
    year = models.IntegerField("Year", null=True, blank=True)
    producer = models.CharField("Producer", max_length=255, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    poster = models.CharField("Poster URL", max_length=500, null=True, blank=True)
    movieLink = models.CharField("Movie URL", max_length=500, null=True, blank=True)
    rating = models.FloatField("Rating", default=1.0, null=True, blank=True)
    genres = models.ManyToManyField(Genre)
    screenshots = models.ManyToManyField('Screenshot', blank=True)
    actors = models.ManyToManyField(Actor, through='Role')
    isTopTen = models.BooleanField("Top 10", default=False, null=True, blank=True)
    isRecommended = models.BooleanField("Recommended", default=False, null=True, blank=True)

    def __str__(self):
        return self.movieName
    
class Screenshot(models.Model):
    movieFrom = models.ForeignKey(Movie, default='', on_delete=models.CASCADE)
    img = models.CharField("URL", default='', max_length=255, null=True, blank=True)
    altText = models.CharField("Alternative Text", default='', max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.pk}) {self.movieFrom.movieName}"
    
class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor} as {self.character} in {self.movie}"