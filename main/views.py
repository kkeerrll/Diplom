from django.shortcuts import render
from .models import Phone
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def massage(request):
    return render(request, 'Massage.html')

def analyzes(request):
    return render(request, 'Analyzes.html')

def sport(request):
    return render(request, 'Sport.html')

def save_phone(request):
    return render(request, 'Save_phone.html')

def save_phone(request):
    if request.method == 'POST':
        phone_number = request.POST['phone']
        phone = Phone(number=phone_number)
        phone.save()
        return render(request, 'Save_phone.html')  # Отобразить страницу успешного сохранения
    else:
        return HttpResponse("Ошибка")
