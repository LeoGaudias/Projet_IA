from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^form/$', views.formulaire, name='formulaire'),
    url(r'^traiter/$', views.traiter, name="traiter"),
    url(r'^$', views.home, name='home'),
]
