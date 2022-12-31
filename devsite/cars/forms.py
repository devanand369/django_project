from django import forms
from .models import Review
from django.forms import ModelForm

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=30)
#     last_name = forms.CharField(label='Last Name', max_length=30)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please write your review here ...',
#                 widget=forms.Textarea(attrs={'class':'myform',
#                 'rows':'2', 'cols':'4'}))

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"      # ['first_name', 'last_name', 'stars']

        labels = {
            'first_name':"YOUR FIRST NAME",
            'last_name':"Last Name",
            'stars':'Rating'
        }

        error_messages = {
            'stars':{
                'min_value':'YO! YO! Min value is 1',
                'max_value':'YO! YO! Max value is 5'

            }
        }
