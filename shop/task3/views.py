from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'third_task/home.html')
def shop(request):
    games = {
        'Game 1': '10.99',
        'Game 2': '15.49',
        'Game 3': '7.99',
    }
    return render(request, 'third_task/shop.html', {'games': games})
def cart(request):
    return render(request, 'third_task/cart.html')