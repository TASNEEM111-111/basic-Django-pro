from django import forms

class LoginForms(forms.Form):
    username = forms.CharField(max_length=100 ,label='name',help_text='enter username' ,required=True)
    password = forms.CharField(max_length=100 , label= 'pass', widget=forms.PasswordInput ,required=True)