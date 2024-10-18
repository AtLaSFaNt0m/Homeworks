from django.shortcuts import render, redirect

# Представление для главной страницы
def main_view(request):
    return render(request, 'fourth_task/main.html')

# Представление для магазина (добавлен список игр)
def shop_view(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    context = {'games': games}
    return render(request, 'fourth_task/shop.html', context)

# Представление для корзины (показывает список игр, добавленных в корзину)
def cart_view(request):
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'fourth_task/cart.html', context)

# Представление с контекстом для списка игр (опционально)
def games_view(request):
    context = {'games': ["Atomic Heart", "Cyberpunk 2077"]}
    return render(request, 'fourth_task/games.html', context)

# Добавить игру в корзину
def add_to_cart(request, game_name):
    # Получаем текущую корзину из сессии или создаём новую как список
    cart = request.session.get('cart', [])

    # Добавляем игру в корзину
    cart.append(game_name)

    # Сохраняем обновлённую корзину в сессии
    request.session['cart'] = cart

    return redirect('/shop/')
