from django.shortcuts import render


def view_vocabulary(response):
    return render(response, "vocabulary/view_vocabulary.html")
