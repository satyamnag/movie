"""
URL configuration for project_movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_movie.views import *
from users.views import *
from django.contrib.auth import views as auth_views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router=routers.SimpleRouter()
router.register(prefix="movies", viewset=MovieViewSet, basename='movies')
router.register(prefix='action_movies', viewset=ActionMovieViewSet, basename='action_movies')
router.register(prefix='drama_movies', viewset=DramaMovieViewSet, basename='drama_movies')
router.register(prefix='crime_movies', viewset=CrimeMovieViewSet, basename='crime_movies')
router.register(prefix='biography_movies', viewset=BiographyMovieViewSet, basename='biography_movies')
router.register(prefix='history_movies', viewset=HistoryMovieViewSet, basename='history_movies')
router.register(prefix='adventure_movies', viewset=AdventureMovieViewSet, basename='adventure_movies')
router.register(prefix='western_movies', viewset=WesternMovieViewSet, basename='western_movies')
router.register(prefix='r_certified_movies', viewset=RCertificationMovieViewSet, basename='R_certified_movies')
router.register(prefix='pg13_certified_movies', viewset=PG13CertificationMovieViewSet, basename='PG13_certified_movies')
router.register(prefix='approved_certified_movies', viewset=ApprovedCertificationMovieViewSet, basename='approved_certified_movies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieListView.as_view(), name='index'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='detail'),
    path('add/', AddMovieView.as_view(), name='add_movie'),
    path('update/<int:movie_id>/', MovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='delete'),
    path('register/', register, name='register'),
    path('activate/<str:uidb64>/<str:token>/', activate, name="activate"),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('profile/', profile, name='profile'),
    path("", include(router.urls)),
    path('api/', api, name='api'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)