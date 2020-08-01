from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    image = models.ImageField(upload_to ='posters/', null=True)
    description = models.CharField(max_length=255)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    
class Comment(models.Model):
    movie_fk = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    predicted = models.CharField(max_length=100)
    probability = models.FloatField()