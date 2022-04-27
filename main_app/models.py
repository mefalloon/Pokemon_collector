from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Poke(models.Model):
	name = models.CharField(max_length=100)
	element = models.CharField(max_length=100)
	attack = models.CharField(max_length=250)
	hp = models.IntegerField()


	def __str__(self):
		return f"The pokemon named {self.name} has id of {self.id}"

	#method
	def get_absolute_url(self):
		return reverse('detail', kwargs={'poke_id': self.id})


FIGHTS = (
    ('B', 'Beginner'),
    ('I', 'Intermediate'),
    ('E', 'Expert'),
)

class Training(models.Model):
    date = models.DateField('training date')
    fight = models.CharField(
	    max_length=1,	
	    choices=FIGHTS,
	    default=FIGHTS[0][0]
	)

    poke = models.ForeignKey(Poke, on_delete=models.CASCADE)

def __str__(self):
	return f"{self.get_fight_display()} on {self.date}"

class Meta:
	ordering = ['-date']

