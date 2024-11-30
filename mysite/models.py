from django.db import models

class About(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='About/images')
    def __str__(self):
        return f"{self.title}"
    
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Portfolio/images')
    def __str__(self):
        return f"{self.title}"
    
class Contact(models.Model):
    name = models.CharField(max_length=250)
    phone_numer = models.CharField(max_length=13)
    email = models.EmailField()
    description = models.TextField()
    def str(self):
        return self.name
