from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Genre
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q

# Create your views here.
def homePage(request):
    return render(request, "primaryFrontend/index.html")

def allPage(request, slug=None):
    genre = None
    movies = Movie.objects.all()
    genres = Genre.objects.order_by('genreName')
    searchData = request.GET.get('search')
    if searchData:
        movies = Movie.objects.filter(Q(movieName__icontains = searchData))
    if slug:
        genre = get_object_or_404(Genre, slug=slug)
        movies = movies.filter(genres__in=[genre])
    return render(request, "primaryFrontend/all.html", {
        'movies': movies,
        'genres': genres,
        'genre': genre
    })
    
def moviePage(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, "primaryFrontend/movie.html", {
        'movie': movie
    })

def topPage(request):
    rMovie = Movie.objects.all()[:1]
    topMovies = Movie.objects.all()[:10]
    return render(request, "primaryFrontend/top.html",{
        'rMovie': rMovie,
        'topMovies': topMovies
    })

def signupPage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginPage")
    else:
        form = NewUserForm()

    return render(request, "user/signup.html", {
        'form': form
    }) 

def loginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect("allPage")

    else:
        form = AuthenticationForm()

    return render(request, "user/login.html", {
        'form': form
    })

def logoutUser(request):
    logout(request)
    return redirect("homePage")