from django import forms
from django.forms import ModelForm
from .models import *

from my_music_app.web.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Album.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class EditAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class DeleteAlbumForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Album
        fields = '__all__'
