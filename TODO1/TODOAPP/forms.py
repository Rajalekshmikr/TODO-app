from . models import Study
from django import forms
class TodoForms(forms.ModelForm):
    class Meta:
        model=Study
        fields=['Topic','Imp_level_of_topic','No_of_revision','date']