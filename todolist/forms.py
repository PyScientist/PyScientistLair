from django import forms


class CreatesNewList(forms.Form):
    name = forms.CharField(label="Name",
                           max_length=200,
                           widget=forms.TextInput(attrs={'size': 35}))
