from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Vocabulary, VocItem
from .forms import CreatesNewVocabularyForm, CreateNewWordForm
import datetime
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='logger.log',
    format='%(asctime)s -,- %(levelname)s -,- %(name)s -,- %(message)s',
    filemode="a",
)


def view_vocabularies_list(request):
    if request.method == 'POST':
        if request.POST.get('create'):
            form = CreatesNewVocabularyForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data["name"]
                voc = Vocabulary(name=name)
                voc.save()
                request.user.vocabulary.add(voc)
        return HttpResponseRedirect('')
    else:
        form = CreatesNewVocabularyForm()

    return render(request,
                  "vocabulary/view_vocabularies_list.html",
                  {'vocabularies': request.user.vocabulary.all(),
                   'response': request,
                   'form': form})


def view_words_in_vocabulary(request, voc_id):
    vocabulary_instance = Vocabulary.objects.get(id=voc_id)

    if request.method == 'POST':
        if request.POST.get("create"):
            form = CreateNewWordForm(request.POST)
            if form.is_valid():
                word = form.cleaned_data["word"]
                main_translation = form.cleaned_data["main_translation"]
                additional_meaning = form.cleaned_data["additional_meaning"]
                word_explanation = form.cleaned_data["word_explanation"]
                vocabulary_instance.vocitem_set.create(word=word,
                               main_translation=main_translation,
                               additional_meaning=additional_meaning,
                               word_explanation=word_explanation)
    else:
        proposed_creation_date = datetime.datetime.now()
        form = CreateNewWordForm(initial={'date_creation': proposed_creation_date})

    context = {
        'form': form,
        'vocabulary': vocabulary_instance,
    }

    return render(request, "vocabulary/view_vocabulary_words.html", context)


def view_word(request, word):

    try:
        user = request.user
        logging.debug(f'user_id is {user.id}')
        word_to_show = VocItem.objects.get(word=word)
        logging.debug(f'word_to_show {word_to_show}')

        context = {
            'word': word_to_show,
        }
    except Exception as err:
        logging.error(err, exc_info=True)

    return render(request, "vocabulary/word_details.html", context)