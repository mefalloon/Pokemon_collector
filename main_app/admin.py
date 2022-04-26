from django.contrib import admin
# import your models here
from .models import Poke, Training

# Register your models here
admin.site.register(Poke)
admin.site.register(Training)