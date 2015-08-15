from django.db import models
from django.contrib.auth.models import User


class HistorySearch(models.Model):
    user = models.ForeignKey(User)
    id_spotify = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    url = models.URLField()

    @classmethod
    def get_distinct_historial(cls, user):
        results = cls.objects.filter(user=user).order_by('-id')
        newresults = []
        seen_altids = []
        for result in results:
            if result.name not in seen_altids:
                seen_altids.append(result.name)
                newresults.append(result)
        return newresults

    def __str__(self):
        return self.user.username + " - " + self.name + " - " + self.type
