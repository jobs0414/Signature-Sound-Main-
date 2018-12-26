from django import forms 

class MusicSearchForm(forms.Form): 
    search_word = forms.CharField(label='Search Word')

    