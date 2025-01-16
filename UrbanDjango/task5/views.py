from django.shortcuts import render
from django.http import HttpResponse

from .forms import UserRegisterForm


users = ['user1', 'user2', 'user3']


def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = 'Пароли не совпадают.'
                return HttpResponse('Пароли не совпадают.')
            elif username in users:
                info['error'] = 'Имя пользователя уже занято.'
                return HttpResponse('Имя пользователя уже занято.')
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет.'
                return HttpResponse('Вы должны быть старше 18 лет.')
            info['welcome_message'] = f"Приветствуем, {username}!"
            return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegisterForm()
        info['message'] = form
    return render(request, 'fifth_task/registration_page.html', {'form': info})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if password != repeat_password:
            info['error'] = 'Пароли не совпадают.'
            return HttpResponse('Пароли не совпадают')
        elif username in users:
            info['error'] = 'Имя пользователя уже занято.'
            return HttpResponse('Пользователь уже существует')
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет.'
            return HttpResponse('Вы должны быть старше 18')
        info['welcome_message'] = f'Приветствуем, {username}!'
        return HttpResponse(f'Приветствуем, {username}!')

    return render(request, 'fifth_task/registration_page.html', context=info)
