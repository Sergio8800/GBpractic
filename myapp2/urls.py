from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views
from .views import *

if settings.DEBUG:
    urlpatterns = [
        path('', index, name='index_start'),
        # path('sum/', views.sum_stock, name='sum_stock'),
        path('user/add/', user_form, name='user_form'),
        path('cat/add/', category_form, name='category_form'),
        path('product/add/', product_form, name='product_form'),
        # path('product/update/<int:product_id>/', product_form_update, name='product_form_update'),
        path('product_del/<int:product_id>/', show_order, name='order'),
        # name='product' на прямую связана get_absolute_url
        path('order/add/', order_form, name='order_form'),
        path('login/', LoginUser.as_view(), name='loginform'),
        path('register/', RegisterUser.as_view(), name='register'),
        path('logout/', logout_user, name='logout'),

        path('product/del/<int:product_id>/', deleteView, name='deleteView'),
        path('orders/', index_orders, name='index_orders'),
        path('orders1/', index_ord_filtr, name='index_ord_filtr'),
        path('product/<int:product_id>/', product_form_update, name='product_form_update'), # name='product' на прямую связана get_absolute_url
        path('order_update/<int:product_id>/', show_order, name='order'),
        # Форма будет доступна по адресу
        # http://127.0.0.1:8000/myapp2/user/add/
        # path('forms/', many_fields_form, name='many_fields_form'),
        # path('forms_w/', many_fields_form_w, name='many_fields_form_w'),
        # path('user/', add_user, name='add_user'),
        # path('upload/', upload_image, name='upload_image'),

    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)