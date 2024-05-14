from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from . import views
from .views import *

if settings.DEBUG:
    urlpatterns = [
        path('', GoodsList.as_view(), name='index_app3'),

        # path('product/del/<int:product_id>/', deleteView, name='deleteView'),


    ]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)