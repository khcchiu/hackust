from django import forms
from django.utils import timezone

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
        self.fields['dataset'] = forms.ChoiceField(
                                            label='Dataset',
                                            required=True,
                                            choices=[('1', 'sample'), ('2', 'all_premade'), ('3', 'all')],
                                            widget=forms.RadioSelect(attrs={'class':'list-unstyled form-check-primary'})
                                        )

class EventForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['staff'] = forms.CharField(label='Which staff? ', widget=forms.Select(choices=[('StaffA', 'StaffA'), ('StaffB', 'StaffB'), ('StaffC', 'StaffC')]))
        self.fields['start'] = forms.DateTimeField(initial=timezone.now(), required=False) 
        self.fields['end'] = forms.DateTimeField(initial=timezone.now(), required=False)
