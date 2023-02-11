from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Vocabulary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="vocabulary", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class VocItem(models.Model):
    vocabulary = models.ForeignKey(Vocabulary, on_delete=models.CASCADE)
    word = models.CharField(max_length=300, default='unknown')
    main_translation = models.CharField(max_length=300, default='unknown')
    additional_meaning = models.CharField(max_length=300, default='unknown')
    word_explanation = models.TextField(default='unknown')
    date_creation = models.DateTimeField(auto_now_add=True)
    on_repeat = models.BooleanField(default=True)
    learned = models.BooleanField(default=False)

    def __str__(self):
        return self.word
