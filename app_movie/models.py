from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    user_name=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    movie_name=models.CharField(max_length=100)
    movie_category=models.CharField(max_length=100)
    movie_releaseyear=models.PositiveIntegerField()
    movie_certificate=models.CharField(max_length=100, default="Nil")
    movie_duration=models.PositiveIntegerField()
    movie_rating=models.DecimalField(max_digits=2, decimal_places=1)
    movie_review=models.DecimalField(max_digits=2, decimal_places=1)
    movie_budget=models.PositiveIntegerField(default=0)
    movie_boxoffice=models.PositiveIntegerField(default=0)
    movie_poster=models.URLField(default="https://png.pngtree.com/element_our/png/20181227/movie-icon-which-is-designed-for-all-application-purpose-new-png_287896.jpg", max_length=1000)
    movie_tagline=models.CharField(max_length=1000, default="Nil")
    movie_description=models.TextField()
    movie_director=models.CharField(max_length=100)
    movie_writers=models.CharField(max_length=100)
    movie_stars=models.CharField(max_length=10000)

    def __str__(self):
        return self.movie_name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk':self.pk})