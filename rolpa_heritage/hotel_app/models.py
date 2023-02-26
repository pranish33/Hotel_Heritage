from django.db import models

# Create your models here.

class Gallery(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField()

    def __str__(self):
        return self.title
    

class Clients(models.Model):
    client_name = models.CharField(max_length=70)
    client_image = models.ImageField()

    def __str__(self):
        return self.client_name
    
class Rating(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    date_created = models.DateField(auto_now_add=True)
    rating_message = models.TextField(blank=False)

    def __str__(self):
        return str(self.id)