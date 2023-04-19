from django import forms


class WordForm(forms.Form):
    wordName = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter Your Word',
        'id': 'semail',
        'name' : 'word'
    }))
