from django.db import models

# Create your models here.

class Comment(models.Model):
    message = models.TextField()

    def __str__(self):
        return str(self.id)
    
  
