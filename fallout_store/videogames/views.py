from django.shortcuts import render

# Главная страница
def index(request):
    return render(request, 'videogames/index.html')

# Список игр
def game_list(request):
    games = [
        {'title': 'Game 1', 'price': 59.99},
        {'title': 'Game 2', 'price': 39.99},
        {'title': 'Game 3', 'price': 49.99},
        # Добавьте больше игр по желанию
    ]
    return render(request, 'videogames/game_list.html', {'games': games})

# Корзина
def cart(request):
    return render(request, 'videogames/cart.html')
