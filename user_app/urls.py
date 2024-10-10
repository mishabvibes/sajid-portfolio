from django.urls import path
from . import views

urlpatterns = [
    path('temp/', views.User_view),
    path('', views.About_section, name='about_section'),
    path('resume/', views.Resume_section, name='resume_section'),
    path('portfolio/', views.Portfolio_section, name='portfolio_section'),
    path('contact/', views.Contact_section, name='contact_section')
]
