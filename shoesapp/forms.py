from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile



class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birth_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female')], required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'birth_date', 'gender')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile.objects.get(user=user)
            profile.birth_date = self.cleaned_data["birth_date"]
            profile.gender = self.cleaned_data['gender']
            profile.save()
            return user
