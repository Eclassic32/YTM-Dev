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
    

class Movie(models.Model):
    movieName = models.CharField("Movie name", max_length=255, null=True, blank=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name="Genre")
    year = models.IntegerField("Year", null=True, blank=True)
    producer = models.CharField("Producer", max_length=255, null=True, blank=True)
    description = models.TextField("Description", null=True, blank=True)
    poster = models.CharField("Poster URL", max_length=500, null=True, blank=True)
    movieLink = models.CharField("Movie URL", max_length=500, null=True, blank=True)
    isTopTen = models.BooleanField("Top 10", default=False, null=True, blank=True)
    isRecommended = models.BooleanField("Recommended", default=False, null=True, blank=True)
    rating = models.FloatField("Rating", default=1.0, null=True, blank=True)

    def __str__(self):
        return self.movieName