from django.conf.urls import patterns, url
from .views import SearchView, SearchArtist

urlpatterns = patterns('',
    url(r'^search/artist', SearchView.as_view(), {'slug': 'artist'}, name='search_artist'),
    url(r'^search/album', SearchView.as_view(), {'slug': 'album'}, name='search_album'),
    url(r'^search/track', SearchView.as_view(), {'slug': 'track'}, name='search_track'),
    url(r'^artist/(?P<artist_id>\w+)/$', SearchArtist.as_view(), name='artist'),
)
