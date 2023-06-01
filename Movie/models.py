from django.db import models

# Create your models here.

class Movie(models.Model):
    rdate = models.DateField()
    movieName = models.CharField(max_length=50)
    hero = models.CharField(max_length=20)
    heroine = models.CharField(max_length=20)
    rating = models.IntegerField()

    def __str__(self) -> str:
        return self.movieName