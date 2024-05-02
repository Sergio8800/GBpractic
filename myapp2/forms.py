import datetime
from .models import Category
from django import forms

# Пользовательская валидация данных с помощью
# метода clean()
# Мы можем прописать свои методы, которые начинаются со слова clean_ и далее
# указать имя поля. Такой метод будет применяться для дополнительной проверки
# поля на корректность.
class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    t_number = forms.CharField(max_length=15)
    adress = forms.CharField(max_length=150)

    def clean_name(self):
        """Плохой пример. Подмена параметра min_length.
        Это антипаттерн. Мы написали пять строк кода, которые делают тоже самое, что и параметр min_length=3."""
        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно содержать не менее 3 символов')
        return name

    # def clean_email(self):
    #     email: str = self.cleaned_data['email']
    #     if not (email.endswith('vk.team') or
    #             email.endswith('corp.mail.ru')):
    #         raise forms.ValidationError('Используйте корпоративную почту')
    #     return email

class CategoryForm(forms.Form):
    name = forms.CharField(max_length=50)

class ProductForm(forms.Form):
    name = forms.CharField(max_length=50)
    category = forms.ModelChoiceField(label = u'категория', queryset = Category.objects.order_by('-name'))
    description = forms.CharField(max_length=15)
    price = forms.FloatField(min_value=12)
    quantity = forms.IntegerField(min_value=12)

class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    # даты приходится вводить вручную:
    # birthdate = forms.DateField(initial=datetime.date.today, widget=forms.DateInput(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'
class ImageForm(forms.Form):
    image = forms.ImageField()