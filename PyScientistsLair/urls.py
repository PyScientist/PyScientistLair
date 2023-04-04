from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("todolist.urls")),
    path('', include("vocabulary.urls")),
    path('', include("register.urls")),
    path('auth/', include('django.contrib.auth.urls')),
]
