from django.shortcuts import render
from django.views import View


# Create your views here.
# Функциональное представление
def function_view(request):
    return render(request, 'second_task/function_template.html')

# Классовое представление
class ClassView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')
