from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

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
    country = CountryField().formfield(
        widget=CountrySelectWidget(
            attrs={
                'class': 'form-control',
            }
        )
    )
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


class EditFoodPostForm(forms.ModelForm):
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
    country = CountryField().formfield(
        widget=CountrySelectWidget(
            attrs={
                'class': 'form-control',
            }
        )
    )
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
        return super(EditFoodPostForm, self).clean(*args, **kwargs)
