from django import forms
from main.models import *

class AnalysisForm(forms.Form):
    """
    location = forms.CharField(max_length=40)
    hashtag = forms.CharField(max_length=40)
    
    class Meta:
        model = Analysis
        fields = ('location', 'hashtag',)
    """
    def __init__(self, *args, **kwargs):
        super(AnalysisForm, self).__init__(*args, **kwargs)
        self.fields['dataset'] = forms.ChoiceField(label='Dataset', required=True,
                                            choices=[('1', 'sample'), ('2', 'all_premade'), ('3', 'all')], widget=forms.RadioSelect)