from django.urls import path

from . import views

urlpatterns = [
    path("view_to_do_lists/to_do_list_<int:id_to_do_list>", views.view_items_in_list_to_do, name="list_to_do"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path("create_to_do_list/", views.create_to_do_list, name="create"),
    path("view_to_do_lists/", views.view_to_do_lists, name="view"),
    path("view_figures/", views.view_figures, name="view_figures")
]