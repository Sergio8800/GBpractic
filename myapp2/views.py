from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import UserForm, CategoryForm, ProductForm, OrderForm
from .models import User, Category, Product, Order


def index(request):
    products = Product.objects.all()
    len_list = len(products)
    print(products[0].name)
    products_lst = []
    for i in range(len_list):
        products_lst.append(products[i])

    # context = {
    #     'name': products.name,
    #     'category': products.category,
    #     'description': products.description,
    #     'price': products.price,
    # }

    return render(request, 'myapp2/index.html', {"products_lst": products_lst})


def index_orders(request):
    products = Order.objects.all()
    context = {
        'title': "Orders of all clients",
        'orders': products,
    }

    return render(request, 'myapp2/index_orders.html', context)

def index_ord_filtr(request):
    today = date.today() - timedelta(days=1)
    order_filtr = Order.objects.filter(date_ordered__gte=today)
    context = {
        'title': "Orders of all clients",
        'diapason': f' не вошли заказы меньше этой даты: {today}',
        'orders': order_filtr,
    }

    return render(request, 'myapp2/index_orders1.html', context)


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

    return render(request, 'myapp2/add_user.html', {'form': form, 'message': message})


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
        message = "Input product"
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


def order_form(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        message = "Error data"
        if form.is_valid():
            customer = form.cleaned_data['customer']
            products = form.cleaned_data['products']
            quantity_prod = form.cleaned_data['quantity_prod']
            total_price = products.price * quantity_prod
            order = Order(customer=customer, products=products, quantity_prod=quantity_prod, total_price=total_price)
            order.save()
            message = f'>>> {order} save in DB'
            # return redirect(category_form)
    else:
        form = OrderForm()
        message = "Input Order"
    return render(request, 'myapp2/order_form.html', {'form': form, 'message': message})
