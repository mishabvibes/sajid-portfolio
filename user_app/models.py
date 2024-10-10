from django.db import models

# Create your models here.


class Portfolio(models.Model) :
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='portfolio_media')
    

    def __str__(self) :
        return '{}'.format(self.title)

class Resume_education(models.Model) :
    education_title = models.CharField(max_length=80) 
    year = models.CharField(max_length=80)
    education_description = models.CharField(max_length=300)

    def __str__(self) :
        return '{}'.format(self.education_title)
    

class Resume_experience(models.Model) :
    experience_title = models.CharField(max_length=80) 
    year = models.CharField(max_length=80)
    experience_description = models.CharField(max_length=300)

    def __str__(self) :
        return '{}'.format(self.experience_title)
    
class Clients(models.Model) :
    clients_logo = models.ImageField(upload_to='client_media')

    def __str__(self) :
        return '{}'.format(self.clients_logo)

