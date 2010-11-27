from django import forms

class SongSearchForm(forms.Form):
    title = forms.CharField()