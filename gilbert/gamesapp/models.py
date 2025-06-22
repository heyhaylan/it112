from django.db import models

# Create your models here.

class Game(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    studio = models.CharField(max_length=50)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title
