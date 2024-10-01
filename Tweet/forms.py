from django import forms 
from .models import *


class TweetForm(forms.ModelForm):
    class META:
        model = Tweet 
        firlds = ['text', 'image']