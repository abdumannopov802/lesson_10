from django.shortcuts import render

# Create your views here.

def homeView(request):
    return render(request, 'home.html', {})

def resumeView(request):
    return render(request, 'resume.html', {})

def portfolioView(request):
    return render(request, 'portfolio.html', {})

def aboutView(request):
    return render(request, 'about.html', {})

def myserviceView(request):
    return render(request, 'service.html', {})

def blogView(request):
    return render(request, 'blog.html', {})

def contactView(request):
    return render(request, 'contact.html', {})