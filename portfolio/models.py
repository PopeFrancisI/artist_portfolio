from datetime import datetime

from django.db import models
from django.utils.text import slugify

from artist_portfolio.settings import STATIC_URL


class Artwork(models.Model):
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artworks')
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)
    year_completed = models.IntegerField(blank=True, default=datetime.now().year)
    technique = models.CharField(max_length=256, blank=True)
    albums = models.ManyToManyField('Album', blank=True)

    def delete(self, using=None, keep_parents=False):
        storage, path = self.image.storage, self.image.path
        super().delete(using, keep_parents)
        storage.delete(path)

    def __str__(self):
        return self.image.name


class Album(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256, default='', editable=False)
    artworks = models.ManyToManyField(Artwork, through=Artwork.albums.through, blank=True)

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

    def get_artworks_count(self):
        artworks_count = self.artworks.count()
        return artworks_count

    def get_artworks_count_ratio(self):
        try:
            album_artwork_count = self.get_artworks_count()
            ratio = album_artwork_count / Artwork.objects.count()
            return ratio
        except Exception as e:
            print(e)
            return 0

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


def get_default_cover():
    return STATIC_URL + 'default_images/default_album_cover.png'
