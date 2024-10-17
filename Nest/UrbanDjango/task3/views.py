from django.shortcuts import render

def index(request):
    return render(request, 'third_task/index.html')

def games(request):
    return render(request, 'third_task/games.html')

def about(request):
    return render(request, 'third_task/about.html')
