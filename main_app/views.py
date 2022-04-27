from django.shortcuts import render, redirect
#import the create view class
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Add the following import
from django.http import HttpResponse
from .models import Poke 
from .forms import TrainingForm
# the template the create view and the update view use is the same 
#templates /<appname
class PokeCreate(CreateView):
    model = Poke
    fields = '__all__'


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
    return render(request, 'about.html')

def pokemon_index(request):
    pokemon = Poke.objects.all()
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})

def pokemon_detail(request, poke_id):
    poke = Poke.objects.get(id=poke_id)
    training_form = TrainingForm()
    
    return render(request, 'pokemon/detail.html', {
    'poke': poke, 'training_form': training_form 
    })

def add_training(request, poke_id):

    #create a model form instance using the data in the request 
    form = TrainingForm(request.POST)
    #validate
    if form.is_valid():
        #do something
        new_training = form.save(commit=False)
        new_training.poke_id = poke_id
        new_training.save()

    return redirect('detail', poke_id=poke_id)