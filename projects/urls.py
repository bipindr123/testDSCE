from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^proposal$', views.proposals, name='proposals'),
    url(r'^search_projects$', views.search_projects, name='search_projects'),
    url(r'^search_proposals$', views.search_proposals, name='search_proposals'),
]
