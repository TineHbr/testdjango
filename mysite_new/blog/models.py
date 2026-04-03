from django.conf import settings
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
       self.published_date = timezone.now()
       self.save()
    
    def __str__(self):
       return self.title

#huiswerk Les 4
class Voetbalspelers(models.Model):
    # De naam van de voetballer en club zijn gewoon tekstvelden
    naam_voetballer = models.CharField(max_length=200) 
    actuele_voetbalclub = models.CharField(max_length=200)
    
    # Foreign key koppelt dit record aan andere tabel i.e. naar de 'user')
    naam_auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)    #mag leeg veld

    #"verzendknop": vult pub_date in & schrijft alles nr db"
    def publish(self):  #actie op dit specifieke object
        self.published_date = timezone.now()    #vervang None/NULL in published_date met huidig tijdstip van deze specifiek speler/object
        self.save() #ingebouwde fctie v models.Model; werk alle gegevens in db bij 

    def __str__(self):  #zichtbaarhd: vervang 'Voetbalspelers object (1) ~ID met naam_voetballer
        return self.naam_voetballer




