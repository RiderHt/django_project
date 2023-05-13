from django import forms
from .models import Categories

class Registration(forms.Form):
    name = forms.CharField(min_length=5, widget=forms.TextInput( attrs={'name': 'name'}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'name':'age'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name':'email'}))

    options = [
        ('m', 'Мужской'),
        ('j', 'Женский')
    ]
    poll = forms.ChoiceField(choices=options, widget=forms.RadioSelect(attrs={'namr':'poll'}))
    password = forms.CharField(min_length=5, widget=forms.PasswordInput(attrs={'name':'password'}))

class Auth(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'name': 'email'}))
    password = forms.CharField(max_length=5, widget=forms.PasswordInput(attrs={'name': 'password'}))

class Addnew(forms.Form):
    title = forms.CharField(min_length=5, widget=forms.TextInput(attrs={'name': 'title'}))
    text = forms.CharField(min_length=5, widget=forms.Textarea(attrs={'name': 'txt'}))
    categories = Categories.objects.all()
    cat = []
    for categori in categories:
        cat.append((categori.name, categori.name))
    cat_res = forms.ChoiceField(choices=cat, widget=forms.RadioSelect(attrs={'name': 'categori'}))
    image = forms.ImageField(widget=forms.FileInput())
    