from django import forms
from .models import SavedList, GunSkin

class ListForm(forms.ModelForm):
    class Meta:
        model = SavedList
        fields = ['guns', 'knives', 'gloves']


class GunExteriorFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        guns = GunSkin.objects.all().values_list('exterior', flat=True)
        for gun in guns:
            self.fields[f'{gun}'] = forms.BooleanField(label=f'{gun}')
            self.fields[f'{gun}'].required = False
