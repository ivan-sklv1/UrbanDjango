from django.shortcuts import render


def main(request):
    title = 'Главная страница'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/main.html', context=context)


def games_list(request):
    title = 'Игры'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'Pay Day 2']
    context = {
        'title': title,
        'text': games,
    }
    return render(request, 'fourth_task/games.html', context)


def cart_list(request):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(request, 'fourth_task/cart.html', context)
