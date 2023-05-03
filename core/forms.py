from django.core.exceptions import ValidationError
from datetime import date
from core import models
from django import forms


class ApplealForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=models.Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label='Службы'
    )

    class Meta:
        model = models.Appeal
        fields = '__all__'


class DeclarerForm(forms.ModelForm):

    class Meta:
        model = models.Declarer
        fields = '__all__'
        widgets = {
            'health_status': forms.Textarea(attrs={'cols': 50, 'rows': 10})
        }

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if len(str(phone)) > 11:
            raise ValidationError('Не может быть длинее 11')
        return phone

    def clean_age(self):
        age = self.cleaned_data['age']
        if age > date.today():
            raise ValidationError('Дата не может быть в будущем')
        return age


class ServiceForm(forms.ModelForm):
    cod = forms.CharField(help_text='Подсказка', label='Код')

    class Meta:
        model = models.Service
        fields = '__all__'




