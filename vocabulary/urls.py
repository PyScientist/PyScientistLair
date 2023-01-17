from django.urls import path
from . import views

urlpatterns = [
    path('view_vocabulary/', views.view_vocabulary, name="vocabulary"),
]