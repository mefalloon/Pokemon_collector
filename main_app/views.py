from django.shortcuts import render
#import the create view class
from django.views.generic.edit import CreateView
# Add the following import
from django.http import HttpResponse
from .models import Poke 

class PokeCreate(CreateView):
    model = Poke
    fields = '__all__'

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return HttpResponse('<h1>About the Pokedex</h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Poke.objects.all()
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def pokemon_detail(request, poke_id):
    poke = Poke.objects.get(id=poke_id)
    return render(request, 'pokemon/detail.html', { 'poke': poke })

