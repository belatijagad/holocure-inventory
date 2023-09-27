from django import forms
from main.models import Idols

class IdolsForm(forms.ModelForm):
    class Meta:
        model = Idols
        fields = ['name', 'branch', 'generation', 'debut_date', 'tagline', 'superchats']