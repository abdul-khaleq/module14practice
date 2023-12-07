from django import forms
from django.forms.widgets import NumberInput
import datetime

class ExampleForm(forms.Form):
    name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField(initial=True)
    date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=['1980', '1981', '1982']))
    value = forms.DecimalField()
    email_address = forms.EmailField(required=False, label='Please enter your email address')
    message = forms.CharField(max_length=10)
    first_name = forms.CharField(initial='Your name')
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect ,choices=[
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),])
    favorite_color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple ,choices=[
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),])
    roll_number = forms.IntegerField(
        help_text='Enter 6 digit roll number'
    )
    pasword = forms.CharField(widget=forms.PasswordInput())