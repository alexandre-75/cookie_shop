from django.shortcuts import render


def homepage(request):
    context = {'extra_css': 'css/homepage.css'}
    return render(request, "homepage.html", context)

def about(request):
    context = {'extra_css': 'css/about.css'}
    return render(request, "about.html", context)