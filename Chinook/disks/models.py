from django.db import models

# Create your models here.

class Artist(models.Model):
    name =models.CharField(max_length=100, verbose_name="Nom de l'artiste")

    class Meta:
        verbose_name = 'Artiste'

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100, verbose_name="Titre de l'album")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Album'

    def __str__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nom du morceau")
    album = models.ForeignKey('Album', on_delete=models.CASCADE, verbose_name="Nom de l'album")
    composer = models.CharField(max_length=100, verbose_name="Nom du compositeur")
    milliseconds = models.IntegerField(verbose_name="Durée")
    bytes = models.IntegerField()
    unitprice = models.FloatField(verbose_name="Prix")

    class Meta:
        verbose_name = 'Morceau'

    def __str__(self):
        return self.name

#un com random