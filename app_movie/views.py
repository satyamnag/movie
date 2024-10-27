from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from django.template import loader
from .forms import MovieForm
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from rest_framework import viewsets
from .serializers import MovieSerializer
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

# def index(request):
#     movie_list=Movie.objects.all()
#     movie_name=request.GET.get('movie_name')
#     if movie_name!='' and movie_name is not None:
#         movie_list=movie_list.fiter(movie_name=movie_name)
#     messages_to_display=messages.get_messages(request)
#     context={
#         'movie_list':movie_list,
#         'messages':messages_to_display,
#     }
#     paginator=Paginator(movie_list, 4)
#     page=request.GET.get('page')
#     movie_list=paginator.get_page(page)
    # return render(request, 'app_movie/index.html', context)

class MovieListView(ListView):
    model=Movie
    template_name='app_movie/index.html'
    context_object_name='movie_list'
    paginate_by=4

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['messages']=messages.get_messages(self.request)
        return context
    
    def get_queryset(self):
        queryset = super().get_queryset()
        movie_name = self.request.GET.get('movie_name')
        if movie_name:
            queryset = queryset.filter(movie_name__icontains=movie_name)
        return queryset

# def detail(request, movie_id):
#     movie=Movie.objects.get(pk=movie_id)
#     context={
#         'movie':movie,
#     }
#     return render(request, 'app_movie/detail.html', context)

class MovieDetailView(DetailView):
    model=Movie
    template_name='app_movie/detail.html'


# def add_movie(request):
#     form=MovieForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, 'app_movie/movie_form.html', {'form':form})


class AddMovieView(CreateView):
    model=Movie
    form_class=MovieForm
    template_name='app_movie/movie_form.html'

    def form_valid(self, form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)


# def update_movie(request, movie_id):
#     movie=Movie.objects.get(id=movie_id)
#     form=MovieForm(request.POST or None, instance=movie)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, 'app_movie/movie_form.html', {'form':form, 'movie':movie})

class MovieUpdateView(UpdateView):
    model=Movie
    form_class=MovieForm
    template_name='app_movie/movie_form.html'

    def get_object(self, queryset=None):
        return Movie.objects.get(id=self.kwargs['movie_id'])
    
    def form_valid(self, form):
        return super().form_valid(form)


# def delete_movie(request, movie_id):
#     movie=Movie.objects.get(id=movie_id)
#     if request.method == 'POST':
#         movie.delete()
#         return redirect('index')
#     return render(request, 'app_movie/movie_delete.html', {'movie':movie})

class MovieDeleteView(DeleteView):
    model=Movie
    template_name='app_movie/movie_delete.html'
    context_object_name='movie'
    success_url=reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

class MovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


class ActionMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_category__icontains='action')
    serializer_class=MovieSerializer

class DramaMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_category__icontains='drama')
    serializer_class=MovieSerializer

class CrimeMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_category__icontains='crime')
    serializer_class=MovieSerializer

class BiographyMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_category__icontains='biography')
    serializer_class=MovieSerializer

class HistoryMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_category__icontains='history')
    serializer_class=MovieSerializer

class AdventureMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_category__icontains='adventure')
    serializer_class=MovieSerializer

class WesternMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_category__icontains='western')
    serializer_class=MovieSerializer

class RCertificationMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_certificate__icontains='R')
    serializer_class=MovieSerializer

class PG13CertificationMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_certificate__icontains='PG-13')
    serializer_class=MovieSerializer

class ApprovedCertificationMovieViewSet(viewsets.ModelViewSet):
    queryset=Movie.objects.filter(movie_certificate__icontains='Approved')
    serializer_class=MovieSerializer


def api(request):
     return render(request, 'app_movie/api.html')
