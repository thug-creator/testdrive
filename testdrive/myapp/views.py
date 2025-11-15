from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm, CARS


users = [
    {'name': 'Костиков Г.',
     'phone': '8(905)345-22-12',
     'email': 'kostikov@gmail.com',
     'car': 'Renault Fluence'},
    {'name': 'Путятин К.А.',
     'phone': '8(905)365-12-12',
     'email': 'putyatin@gmail.com',
     'car': 'Cadilac Escalade ESV Sport Platinum'},
    {'name': 'Стародубова Д.Д.',
     'phone': '8(905)335-22-22',
     'email': 'starodubova@gmail.com',
     'car': 'Audi RS7 Perfomance'}
]


def index(request):
    return render(request, "index.html", context={'users': users})


def about(request):
    return render(request, "about.html")


def testdrive(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            phone = userform.cleaned_data['phone']
            email = userform.cleaned_data['email']
            datatime = userform.cleaned_data['datatime']
            car = int(userform.cleaned_data['car'])
            coment = userform.cleaned_data['coment']
            car = list(filter(lambda elem: elem[0] == car, CARS))[0][1]
            users.append({'name': name,
                          'phone': phone,
                          'email': email,
                          'car': car,
                         'datatime': datatime})
        else:
            return HttpResponse('Invalid data')
    userform = UserForm()
    return render(request, "testdrive.html", {'form': userform})
