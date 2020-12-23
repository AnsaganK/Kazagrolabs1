from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SelectionForm(forms.ModelForm):
    class Meta:
        model = Selection
        fields = ('nameClient','samples','countSamples','date','status')


class PreparationForm(forms.ModelForm):
    class Meta:
        model = Preparation
        fields = ('nameClient','samples','countSamples','selfParent','date','status')

class LaboratoryForm(forms.ModelForm):
    class Meta:
        model = Laboratory
        fields = ('nameClient','samples','countSamples','selfParent','date','status')

class AgrohymForm(forms.ModelForm):
    class Meta:
        model = Agrohym
        fields = ('nameClient','samples','countSamples','date','status')

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Логин')
    #email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'groups')


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'countSamples', 'date')

class ClientCormForm(forms.ModelForm):
    class Meta:
        model = ClientCorm
        fields = ('name', 'date')

class SampleForm(forms.ModelForm):
    class Meta:
        model = Samples
        fields = '__all__'

class ElementForm(forms.ModelForm):
    class Meta:
        model =elementsName
        fields = '__all__'

class CormsForm(forms.ModelForm):
    class Meta:
        model = Corms
        fields = '__all__'