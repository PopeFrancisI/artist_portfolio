from django import views
from django.http import response
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

    def get(self, request):
        # TODO: pass artworks matching album in context
        context = {}
        return render(request, template_name='album.html')
