from django.shortcuts import render
from .models import Visit
# Create your views here.

def visits_page(request):
    error = ''

    if request.method == 'POST':
        name = request.POST.get('user_name')

        if len(name) < 5 or name.isdecimal():
            error = 'Недоступное имя'

        elif Visit.objects.filter(name=name).exists():
            error = 'Такое имя уже занято'

        else:
            error= 'Имя успешно добавленно'
            Visit.objects.create(name=name)

    return render(request, 'project/index.html', {'error': error})