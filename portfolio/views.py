from django import views
from django.shortcuts import render
from django.views.generic import ListView
from portfolio import models
from portfolio.models import Album, Artwork


class IndexView(views.View):

    def get(self, request):
        artworks = models.Artwork.objects.all()
        context = {'artworks': artworks}
        return render(request, template_name='index.html', context=context)


class GalleryView(ListView):
    model = Album
    ordering = 'title'
    template_name = 'gallery.html'


class AlbumView(views.View):

    def get(self, request, title):
        artworks = Artwork.objects.filter(album__title=title)
        print(artworks)
        context = {'album_artworks': artworks}
        return render(request, template_name='album.html', context=context)
