from django import views
from django.http import response
from django.shortcuts import render
from django.views.generic import ListView

from portfolio import models
from portfolio.models import Album


class IndexView(views.View):

    def get(self, request):
        artworks = models.Artwork.objects.all()
        context = {'artworks': artworks}
        return render(request, template_name='index.html', context=context)


class GalleryView(ListView):
    model = Album
    ordering = 'title'
    template_name = 'gallery.html'
