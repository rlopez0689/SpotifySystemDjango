from django.conf.urls import patterns, url
from .views import LoginView, ProfileView, logout_view, RegisterView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', logout_view),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^profile/$', ProfileView.as_view(), name='profile'),
)
