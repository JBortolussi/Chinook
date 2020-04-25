from django.shortcuts import render, get_object_or_404, redirect
from disks.models import Album, Artist, Track
from django.http import Http404
# Create your views here.

def home(request, album_id=1):
    if ("titre" in request.GET):
        titre = request.GET['titre']
        albums = Album.objects.using('chinook').filter(title__contains=titre)
        if (not albums.filter(id=album_id)): #on test si l'article selectionné est dans la recherche
            if (albums):
                album_display = albums[0]
                tracks = Track.objects.using('chinook').filter(album=album_display)
            else:
                titre=''
                album_display = None
            return render(request, "disks/home.html", locals())
    else:
        titre = ''
        albums = Album.objects.using('chinook').all()

    if (album_id != None):
        try:
            album_display=albums.get(id=album_id)
            tracks = Track.objects.using('chinook').filter(album=album_display)
        except Album.DoesNotExist:
            raise Http404
    else:
        album_display=None

    return render(request, "disks/home.html", locals())

def home_search_select(request, album_id, titre):
    albums = Album.objects.using('chinook').filter(title__contains=titre)
    if (not albums.filter(id=album_id)):  # on test si l'article selectionné est dans la recherche
        album_display = None
        return render(request, "disks/home.html", locals())

    try:
        album_display = albums.get(id=album_id)
        tracks = Track.objects.using('chinook').filter(album=album_display)
    except Album.DoesNotExist:
        raise Http404

    return render(request, "disks/home.html", locals())