from django import forms
from django.forms import ModelForm
from .models import *

from online_library_app.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First Name',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last Name',
                }
            ),
            'profile_image_url': forms.URLInput(
                attrs={
                    'placeholder': 'URL',
                }
            ),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Book.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = "__all__"


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    "rows": 5,
                }
            ),
            'book_image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }
            ),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime..',
                }
            ),

        }


class EditBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


