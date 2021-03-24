from portfolio.models import Album


def album_renderer(request):
    return {'albums': Album.objects.all()}
