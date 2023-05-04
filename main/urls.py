from django.urls import path
from django.views.generic.base import RedirectView
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", RedirectView.as_view(url="/"), name="no_list"),
    path("list/<int:list_id>/", views.list_site, name="list"),
    path("add/", views.add, name="add"),
]
