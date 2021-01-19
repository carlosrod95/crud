"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from app.models import Historial  


class HistorialForm(forms.ModelForm):
    Calif_Parcial_1 = forms.CharField(label='CALIFICACIONES PARCIAL 1', max_length=3)
    Calif_Parcial_2 = forms.CharField(label='CALIFICACIONES PARCIAL 2', max_length=3)
    Calif_Parcial_3 = forms.CharField(label='CALIFICACIONES PARCIAL 3', max_length=3)
    class Meta:  
        model = Historial  
        #fields = "__all__"  
        fields ="Calif_Parcial_1","Calif_Parcial_2","Calif_Parcial_3"




class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
