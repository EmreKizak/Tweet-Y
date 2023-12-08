from django import forms
from .models import Tweet

class AddTweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['username','nickname', 'message', 'image']
    