from core import models
from django import forms


class ApplealForm(forms.ModelForm):

    class Meta:
        model = models.Appeal
        fields = '__all__'


class DeclarerForm(forms.ModelForm):

    class Meta:
        model = models.Declarer
        fields = '__all__'


class ServiceForm(forms.ModelForm):

    class Meta:
        model = models.Service
        fields = '__all__'


