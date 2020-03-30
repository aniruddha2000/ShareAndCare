from django import forms

from . import models


class FoodPostForm(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Excess food by default',
            'style': 'border-radius: 4px;',
        }
    ), )
    description = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'description...',
            'style': 'border-radius: 4px;',
        }
    ), )
    country = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'country...',
            'style': 'border-radius: 4px;',
        }
    ), )
    city = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'City...',
            'style': 'border-radius: 4px;',
        }
    ), )
    address = forms.CharField(label='', widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Address...',
            'style': 'border-radius: 4px;',
        }
    ), )

    class Meta:
        model = models.FoodPost
        fields = [
            'title', 'description', 'country', 'city', 'address',
        ]

    def clean(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        description = self.cleaned_data.get('description')
        country = self.cleaned_data.get('country')
        city = self.cleaned_data.get('city')
        address = self.cleaned_data.get('address')
        return super(FoodPostForm, self).clean(*args, **kwargs)
