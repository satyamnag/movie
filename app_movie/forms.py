from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    movie_name=forms.CharField(label="Movie Name:", max_length=100)
    movie_category=forms.CharField(label='Category:', max_length=100)
    movie_releaseyear=forms.CharField(label="Release Year:", max_length=100)
    movie_certificate=forms.CharField(label="Certificate", max_length=100)
    movie_duration=forms.CharField(label="Duration:", max_length=100)
    movie_rating=forms.CharField(label="Rating:", max_length=100)
    movie_review=forms.CharField(label="Reviews:", max_length=100)
    movie_budget=forms.CharField(label="Budget")
    movie_boxoffice=forms.CharField(label="Box Office")
    movie_poster=forms.CharField(label="Poster:", max_length=1000)
    movie_tagline=forms.CharField(label="Tagline", max_length=1000)
    movie_description=forms.CharField(label="Short Description:", max_length=1000)
    movie_director=forms.CharField(label="Director/s:", max_length=100)
    movie_writers=forms.CharField(label="Writer/s:", max_length=100)
    movie_stars=forms.CharField(label="Star/s:", max_length=10000)
    
    class Meta:
        model=Movie
        fields=["movie_name",
                "movie_category",
                "movie_releaseyear",
                "movie_certificate",
                "movie_duration",
                "movie_rating",
                "movie_review",
                "movie_budget",
                "movie_boxoffice",
                "movie_poster",
                "movie_tagline",
                "movie_description",
                "movie_director",
                "movie_writers",
                "movie_stars"]