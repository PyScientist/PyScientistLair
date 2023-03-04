from django.contrib import admin
from .models import VocItem, Vocabulary

# Register your models here.
admin.site.register(Vocabulary)
admin.site.register(VocItem)
