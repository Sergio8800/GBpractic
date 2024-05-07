import datetime

from django.utils.safestring import SafeString

from .models import Category, User, Product, Order
from django import forms


# Пользовательская валидация данных с помощью
# метода clean()
# Мы можем прописать свои методы, которые начинаются со слова clean_ и далее
# указать имя поля. Такой метод будет применяться для дополнительной проверки
# поля на корректность.
class UserForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # class on every div when I use {{ form.as_div }} on html template
    def as_div(self):
        return SafeString(super().as_div().replace("<div>", "<div class='form-group'>"))

    name = forms.CharField(max_length=50, label='Login', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    t_number = forms.CharField(max_length=15, label='phone namber')
    adress = forms.CharField(max_length=150, label='adress', required=False)

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


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "not category"

    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'category', 'description']



class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['customer'].empty_label = "not user"
        self.fields['products'].empty_label = "not product"

    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['customer', 'products', 'quantity_prod']
        # widgets = {
        #     'customer': forms.TextInput(attrs={"class": "form-control", "placeholder": "Имя" }),
        #
        #     'products': forms.TextInput(attrs={"class": "form-control", "placeholder": "Товар"}),
        #     'quantity_prod': forms.IntegerField(attrs={"class": "form-control", "placeholder": "Количество"}),
        # }


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
