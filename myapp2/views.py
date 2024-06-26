from datetime import date, timedelta

from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *
from .models import User, Category, Product, Order


def index(request):
    products = Product.objects.all().order_by('-date_added')
    context = {
        'title': "Orders of all clients",
        'products': products,
    }

    return render(request, 'myapp2/index.html', context=context)
    # return render(request, 'myapp2/index.html', {"products_lst": products_lst})


def index_orders(request):
    products = Order.objects.all()
    context = {
        'title': "Orders of all clients",
        'orders': products,
    }

    return render(request, 'myapp2/index_orders.html', context=context)


def index_ord_filtr(request):
    today = date.today() - timedelta(days=1)
    order_filtr = Order.objects.filter(date_ordered__gte=today)
    # order_filtr = Order.objects.exclude(date_ordered__gte=today) # исключить все записи удовлетворяющие условию
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
            # form.save()
            message = 'Пользователь сохранён'
    else:
        form = UserForm()
        message = 'Заполните форму'

    return render(request, 'myapp2/add_user.html', {'form': form, 'message': message})


def product_form(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        message = "Error data"
        if form.is_valid():
            # name = form.cleaned_data['name']
            # category = form.cleaned_data['category']
            # description = form.cleaned_data['description']
            # price = form.cleaned_data['price']
            # quantity = form.cleaned_data['quantity']
            # image = form.cleaned_data['image']
            # print(image)
            # # fs = FileSystemStorage()
            # # fs.save(image.name, image)
            # product = Product(name=name, category=category, description=description, price=price,
            #                   quantity=quantity, image=image)
            # product.save()
            form.save()
            return redirect(product_form)
    else:
        form = ProductForm()
        message = "Input product"
    return render(request, 'myapp2/product_form.html', {'form': form, 'message': message})


def product_form_update(request, product_id):
    # intention = Product.objects.get(pk=product_id)
    intention = get_object_or_404(Product, pk=product_id)
    message = 'change data'
    form = ProductForm(instance=intention)  # important for entre DATA
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # important for entre DATA

        if form.is_valid():
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            quantity = form.cleaned_data['quantity']
            image = form.cleaned_data['image']
            fs = FileSystemStorage()

            Product.objects.filter(pk=product_id).update(name=name, category=category, description=description,
                                                         price=price, quantity=quantity,
                                                         image=fs.save(image.name, image))

            message = ' data is change '
            # return redirect('index_start')

    return render(request, 'myapp2/product_form_update.html', {'form': form, 'message': message})


def deleteView(request, product_id):
    obj = Product.objects.get(pk=product_id)
    if request.method == 'POST':
        obj.delete()
        return redirect('index_start')
    template_name = 'myapp2/product_del.html'
    context = {'obj': obj}
    return render(request, template_name, context)


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


def show_order(request, product_id):
    # if request.method == 'POST':
    #     form = OrderForm(request.POST)
    #     message = "Error data"
    #     if form.is_valid():
    #         customer = form.cleaned_data['customer']
    #         products = form.cleaned_data['products']
    #         quantity_prod = form.cleaned_data['quantity_prod']
    #         total_price = products.price * quantity_prod
    #         order = Order(customer=customer, products=products, quantity_prod=quantity_prod, total_price=total_price)
    #         order.save()
    #         message = f'>>> {order} save in DB'
    #         # return redirect(category_form)
    # else:
    #     form = OrderForm()
    #     message = "Input Order"
    # return render(request, 'myapp2/order_form.html', {'form': form, 'message': message})

    return HttpResponse(f"Отображение товара с id = {product_id}")


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'myapp2/register.html'
    success_url = reverse_lazy('loginform')

    # эта функция для автоматической аунтификации на сате после регистрации.
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index_start')
    #     # form.instance.created_by = self.request.user
    #     # return super().form_valid(form)
    #
    #     # valid = super(CreateArtistView, self).form_valid(form)
    #     user, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
    #     print(user,password)
    #     new_user = authenticate(username=user, password=password)
    #     login(self.request, new_user)
    #     return redirect('index_start')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'myapp2/login.html'

    def get_success_url(self):
        return reverse_lazy('index_start')


def logout_user(request):
    logout(request)
    return redirect('loginform')
