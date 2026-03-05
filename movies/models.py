from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 11)])

    def __str__(self):
        return self.title
