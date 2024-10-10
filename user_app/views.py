from django.shortcuts import render
from .models import Portfolio,Resume_education,Resume_experience, Clients
# Create your views here.


def User_view(request) :
    return render(request, 'index.html')


def About_section(request) :
    clients = Clients.objects.all()
    return render(request, 'about.html', {'clients':clients})


def Resume_section(request) :
    educations = Resume_education.objects.all()
    experiences = Resume_experience.objects.all()

    context = {'educations':educations,
               'experiences':experiences
               }
    
    return render(request, 'resume.html',context)


def Portfolio_section(request) :
    portfolios = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'portfolios':portfolios})

def Contact_section(request) :
    return render(request, 'contact.html')