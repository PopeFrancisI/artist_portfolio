from django.db import models


class Artwork(models.Model):
    title = models.CharField(max_length=256, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artworks')
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.image.name
