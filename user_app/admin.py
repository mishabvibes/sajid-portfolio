from django.contrib import admin
from .models import Portfolio, Resume_education, Resume_experience,Clients
from unfold.admin import ModelAdmin as UnfoldModelAdmin

# Register Portfolio model in the admin panel
@admin.register(Portfolio)
class PortfolioAdmin(UnfoldModelAdmin):
    list_display = ('title', 'image')

# Register Resume_education model in the admin panel
@admin.register(Resume_education)
class ResumeEducationAdmin(UnfoldModelAdmin):
    list_display = ('education_title', 'year')

# Register Resume_experience model in the admin panel
@admin.register(Resume_experience)
class ResumeExperienceAdmin(UnfoldModelAdmin):
    list_display = ('experience_title', 'year') 

# Register Clients model in the admin panel
@admin.register(Clients)
class ClientsAdmin(UnfoldModelAdmin):
    list_display = ('clients_logo',) 
