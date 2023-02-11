from django.urls import path
from . import views

urlpatterns = [
    path('view_vocabularies_list/',
         views.view_vocabularies_list,
         name="vocabulary_list"),
    path('view_vocabularies_list/words_list_<int:voc_id>',
         views.view_words_in_vocabulary,
         name="vocabulary_words"),
    path('view_vocabularies_list/word_<str:word>',
         views.view_word,
         name="view_word")
]
