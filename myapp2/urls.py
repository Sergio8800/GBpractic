
from django.contrib import admin
from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', index, name='index_start'),
    # path('sum/', views.sum_stock, name='sum_stock'),
    path('user/add/', user_form, name='user_form'),
    path('cat/add/', category_form, name='category_form'),
    path('product/add/', product_form, name='product_form'),
    path('order/add/', order_form, name='order_form'),
    path('orders/', index_orders, name='index_orders'),
    path('orders1/', index_ord_filtr, name='index_ord_filtr'),
    # Форма будет доступна по адресу
    # http://127.0.0.1:8000/myapp2/user/add/
    # path('forms/', many_fields_form, name='many_fields_form'),
    # path('forms_w/', many_fields_form_w, name='many_fields_form_w'),
    # path('user/', add_user, name='add_user'),
    # path('upload/', upload_image, name='upload_image'),

]
