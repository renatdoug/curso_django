from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'texto': 'tentado aprender Django',
    })


def recipe(request, id):
    return render(request, 'recipes/pages/home.html', context={
        'texto': 'Renato Douglas',
    })
