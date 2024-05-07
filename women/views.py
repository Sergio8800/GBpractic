from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect
from .form import WomenForm
from .models import *
from django import db

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Добавить женщину", 'url_name': 'add_women'},
        {'title': "Войти", 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    print(posts)
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница'
    }

    return render(request, 'women/index.html', context=context)

def add_woman(request):
    if request.method == 'POST':
        form = WomenForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            user = Women(title=title, content=content)
            db.connections.close_all()
            user.save()
            message = f'{user} сохранён'
    else:
        form = WomenForm()
        message = 'Заполните форму'

    return render(request, 'women/add_women.html', {'form': form, 'message': message})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О сайте'})


def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьиИИИ с id = {post_id}")
