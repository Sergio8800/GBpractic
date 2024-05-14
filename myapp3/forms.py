from django import forms
# from snowpenguin.django.recaptcha3.fields import ReCaptchaField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class AddCar(forms.ModelForm):
    class Meta:
        model = Car
        fields = ("author", "title", "genres", "category", "fuel", "price", "poster")
        widgets = {'author': forms.HiddenInput()}
        # def __init__(self, *args,**kwargs):
        #     super().__init__(*args,**kwargs)
        #     for field in self.fields:
        #         self.fields[field].widget.attrs['class'] = 'form-control'

#ЗАГРУСКА НЕСКОЛЬКИХ ФОТО НЕ РАБОТАЕТ
# class AddCarImage(forms.ModelForm):
#     # name = forms.CharField(label=u'Локация')
#     # photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))
#     class Meta:
#         model = CarShorts
#         fields = ("car", "image")
#         widgets = {'image': forms.FileInput(attrs={'multiple': 'multiple'})}
#         widgets = {'car': forms.HiddenInput()}


class AuthForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "password")


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("username", "password", "email")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
