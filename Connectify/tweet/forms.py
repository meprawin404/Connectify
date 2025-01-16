from django import forms
from .model import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = tweet
        fields = ['text', 'photo']
