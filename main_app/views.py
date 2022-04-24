from django.shortcuts import render

# Add the following import
from django.http import HttpResponse
#Add the Cat class & list and view function below the imports
class Poke:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, attack, hp):
    self.name = name
    self.breed = breed
    self.attack = attack
    self.hp = hp

pokemon = [
    Poke('Charizard', 'fire', 'Fire spin', 150),
    Poke('Pikachu', 'electric', 'thunderbolt', 190),
    Poke('Beedrill', 'grass', 'Poison sting', 80)
]

# Define the home view
def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return HttpResponse('<h1>About the Pokedex</h1>')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html', {'pokemon': pokemon})