from django.forms import ModelForm
from .models import SavedList

class ListForm(ModelForm):
    class Meta:
        model = SavedList
        fields = ['guns', 'knives', 'gloves']