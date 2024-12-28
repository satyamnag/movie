from django.contrib import admin
from .models import Movie

# Register your models here.

admin.site.site_header='Movies'
admin.site.site_title='Movies'
admin.site.index_title='Manage Movies'

class MovieAdmin(admin.ModelAdmin):

    def user_admin(self, request, queryset):
        queryset.update(user_name="Site Admin")

    user_admin.short_description="Update User Name to Site Admin"
    list_display=('movie_name', 'user_name', 'movie_category', 'movie_releaseyear', 'movie_certificate', 'movie_duration', 'movie_rating', 'movie_review', 'movie_budget', 'movie_boxoffice')
    search_fields=('movie_name',)
    actions=('user_admin',)

admin.site.register(Movie, MovieAdmin)