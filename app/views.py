from django.shortcuts import render


def contact(request):
    return render(request,'app/contact.html')

def index(request):
    return render(request,'app/index.html')

def portfolio(request):
    return render(request,'app/portfolio.html')

def resume(request):
    return render(request,'app/resume.html')