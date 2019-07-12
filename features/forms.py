from django import forms
from .models import Feature


class featureForm(forms.ModelForm):

    class Meta:
        model = Feature
        fields = ('featureName','description', 'price', 'published_date')