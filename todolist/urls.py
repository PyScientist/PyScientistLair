from django.urls import path

from . import views

urlpatterns = [
    path("view_to_do_lists/to_do_list_<int:id_to_do_list>", views.view_items_in_list_to_do, name="list_to_do_items"),
    path("home/", views.home, name="home"),
    path("", views.home, name="home"),
    path("view_to_do_lists/", views.view_to_do_lists, name="view_to_do_lists"),
    path("view_images/", views.view_images, name="view_images"),
    path("view_portfolio/", views.view_portfolio, name="view_portfolio"),
]