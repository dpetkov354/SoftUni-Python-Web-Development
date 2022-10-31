from django import forms
from game_play_app.web.models import Profile, Game


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ("email", "age", "password")


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Game.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = '__all__'
