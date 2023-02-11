from django import forms


class CreatesNewVocabularyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)

    def __init__(self, *args, **kwargs):
        super(CreatesNewVocabularyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['style'] = 'width: 320px;'

class CreateNewWordForm(forms.Form):
    word = forms.CharField(label='Word', max_length=300)
    main_translation = forms.CharField(label='Translation', max_length=300)
    additional_meaning = forms.CharField(label='Additional meanings', max_length=300)
    word_explanation = forms.CharField(label='Explanation', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(CreateNewWordForm, self).__init__(*args, **kwargs)
        self.fields['word'].widget.attrs['style'] = 'width: 100%; height:35px;'
        self.fields['main_translation'].widget.attrs['style'] = 'width: 100%; height:35px;'
        self.fields['additional_meaning'].widget.attrs['style'] = 'width: 100%; height:35px;'
