from django.contrib import admin
from .models import Genre, Movie, Actor, Character, Screenshot, Role

# Register your models here.
admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Character)
admin.site.register(Screenshot)
admin.site.register(Role)
