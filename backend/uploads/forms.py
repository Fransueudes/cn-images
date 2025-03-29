'''from django import forms
from .models import Arquivo

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['nome', 'arquivo']
'''
from django import forms
from .models import Arquivo

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']
