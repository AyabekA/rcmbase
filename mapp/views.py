from django.shortcuts import render


def mapp(request):
    return render(request, 'mapp/mapp.html')
