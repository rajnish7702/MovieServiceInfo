from django.shortcuts import render
from Movie.forms import MovieForm
from Movie.models import Movie

# Create your views here.

def index(request):
    return render(request,'movie/index.html')
def addmovie(request):
    form = MovieForm()
    if request.method=='POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    return render(request,'movie/addmovie.html',{'form':form})
def listmoves(request):
    movie_list=Movie.objects.all().order_by('-rating')
    return render(request,'movie/listmovie.html',{'movie_list':movie_list})


    
