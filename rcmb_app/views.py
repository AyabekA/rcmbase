from django.shortcuts import render

def title(request):
    return render(request, "rcmb_app/title.html", {})