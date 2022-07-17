from django.db import models

# Create your models here.
class Countrie(models.Model):
    nombre= models.CharField(max_length=60, blank=True, default='')
    capital= models.CharField(max_length=60, blank=True, default='')

    class Meta:
        ordering = ('id',)


    def __str__(self):
        return self.nombre