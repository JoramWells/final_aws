from dataclasses import field
from django import forms
from .models import *

class InputForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter image name'
    }))
    prefix = 'pepper'
    
    class Meta:
        model = Pepper
        fields = ['name','image']
        
        
class TomatoForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control','placeholder':'Enter potato dsease name'
    }))
    prefix = 'tomato'
    
    
    class Meta:
        model = Tomato
        fields = ['name','image']
        
class PotatoForm(forms.ModelForm):   
    
    class Meta:
        model = Potato
        fields = ['image']