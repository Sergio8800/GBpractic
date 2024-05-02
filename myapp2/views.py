from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm, CategoryForm, ProductForm
from .models import User, Category, Product


def sum_stock(request):
    return HttpResponse('<h1>Hello word</h1>')


def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            t_number = form.cleaned_data['t_number']
            adress = form.cleaned_data['adress']
            # Делаем что-то с данными
            # logger.info(f'Получили {name=}, {email=}, {adress=}.')
            user = User(name=name, email=email, t_number=t_number, adress=adress)
            user.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'

    return render(request, 'myapp2/user_form.html', {'form': form, 'message': message})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        message = "Error data"
        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            product = Product(name=name, category=category, description=description, price=price, quantity=quantity)
            product.save()
            form.clean()
            return redirect(product_form)
    else:
        form = ProductForm()
        message = "Input category"
    return render(request, 'myapp2/product_form.html', {'form': form, 'message': message})


def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        message = "Error data"
        if form.is_valid():
            name = form.cleaned_data['name']
            cat = Category(name=name)
            cat.save()
            form.clean()
            message = f'Категория {cat.name} save in DB'
            # return redirect(category_form)
    else:
        form = CategoryForm()
        message = "Input category"
    return render(request, 'myapp2/category_form.html', {'form': form, 'message': message})
