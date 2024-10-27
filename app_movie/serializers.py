from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields=['id',
                'movie_name',
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