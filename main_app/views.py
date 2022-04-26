from django.shortcuts import render
#import the create view class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse
from .models import Poke 
# the template the create view and the update view use is the same 
#templates /<appname
class PokeCreate(CreateView):
    model = Poke
    fields = '__all__'
    success_url = '/pokemon/'

class PokeUpdate(UpdateView):
    model = Poke
    # Let's disallow the renaming of a cat by excluding the name field!
    fields = ['element', 'attack', 'hp']

class PokeDelete(DeleteView):
    model = Poke
    success_url = '/pokemon/'

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

