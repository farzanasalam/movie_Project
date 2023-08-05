from django.shortcuts import render, redirect
from .models import movie
from .forms import movieForm


# Create your views here.

def index(request):
    Movie = movie.objects.all()
    context = {
        'Movie_list': Movie
    }
    return render(request, "index.html", context)


def detail(request, movie_id):
    movie1 = movie.objects.get(id=movie_id)
    return render(request, "detail.html", {"movie1": movie1})


def add_movie(request):
    if request.method == "POST":
        name = request.POST.get("name", )
        desc = request.POST.get("desc", )
        year = request.POST.get("year", )
        img = request.FILES["img"]
        Movie1 = movie(name=name, desc=desc, year=year, img=img)
        Movie1.save()
    return render(request, "add_movie.html", {"Movie1": Movie1})


def update(request, id):
    movie2 = movie.objects.get(id=id)
    form = movieForm(request.POST or None, request.FILES, instance=movie2)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html', {'form': form, 'movie': movie2})


def delete(request, id):
    if request.method == 'POST':
        Movie = movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request, "delete.html")
