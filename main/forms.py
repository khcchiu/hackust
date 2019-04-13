from django import forms
from main.models import *

class AnalysisForm(forms.ModelForm):
    location = forms.CharField(max_length=40)
    hashtag = forms.CharField(max_length=40)
    
    class Meta:
        model = Analysis
        fields = ('location', 'hashtag',)