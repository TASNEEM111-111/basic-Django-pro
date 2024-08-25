from django import forms
from .models import Login

class ModelForm(forms.ModelForm):
    class Meta:
        model = Login
        fields =['username']