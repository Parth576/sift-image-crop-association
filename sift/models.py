from django.db import models

# Create your models here.

class im(models.Model):
    image=models.ImageField(upload_to='../media/images/')
    crops=models.ImageField(upload_to='../media/crops/')

    def __str__(self):
        return 'Image'
