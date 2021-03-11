from django import views
from django.http import response
from django.shortcuts import render

from portfolio import models


class IndexView(views.View):

    def get(self, request):
        artworks = models.Artwork.objects.all()
        context = {'artworks': artworks}
        return render(request, template_name='index.html', context=context)
