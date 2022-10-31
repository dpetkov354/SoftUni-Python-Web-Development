from django import forms
from regular_exam_app.web.models import Profile, Car


class CreateProfileForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ("user_name", "email", "age", "password",)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


class DeleteProfileForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Profile.objects.all().delete()
            Car.objects.all().delete()
        return self.instance

    class Meta:
        model = Profile
        fields = ()


class CreateCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"


class DeleteCarForm(forms.ModelForm):

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Car.objects.all().delete()
        return self.instance

    class Meta:
        model = Car
        fields = "__all__"
