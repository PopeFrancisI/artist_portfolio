from django.db import models
from django.utils.text import slugify

from artist_portfolio.settings import STATIC_URL


class Artwork(models.Model):
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artworks')
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name


class Album(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='', editable=False)
    artworks = models.ManyToManyField(Artwork, blank=True)

    def get_cover_url(self):
        newest_artwork = self.get_newest_artwork()
        if newest_artwork:
            return newest_artwork.image.url
        else:
            return get_default_cover()

    def get_newest_artwork(self):
        try:
            newest_artwork = self.artworks.latest('time_created')
            return newest_artwork
        except Exception:
            return None

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def get_default_cover():
    return STATIC_URL + 'default_images/default_album_cover.png'
