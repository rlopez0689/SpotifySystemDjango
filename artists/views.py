from django.shortcuts import render
from django.views.generic import View

from userprofiles.mixins import LoginRequiredMixin
from .models import HistorySearch
import requests


class SearchView(LoginRequiredMixin, View):
    template_name = 'artist_form.html'

    def get(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        return render(request, self.template_name, {'slug': slug})

    def post(self, request, *args, **kwargs):
        slug = kwargs.get("slug")
        r = requests.get("https://api.spotify.com/v1/search?q="+request.POST['artist']+"&type="+slug+"")
        results = dict()
        results['response'] = r.json()
        return render(request, self.template_name, {'results': results, 'slug': slug})


class SearchArtist(LoginRequiredMixin, View):
    template_name = 'artist_show.html'

    def get(self, request, artist_id):
        albums = requests.get("https://api.spotify.com/v1/artists/"+artist_id+"/albums")
        r = requests.get("https://api.spotify.com/v1/artists/"+artist_id)
        results = dict()
        results['albums'] = albums.json()
        results['response'] = r.json()
        hs = HistorySearch(user=self.request.user, type='artist', name=results['response']['name'], url='/artist/'+artist_id)
        hs.save()
        return render(request, self.template_name, {'results': results})
