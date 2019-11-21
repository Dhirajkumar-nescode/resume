from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    dop = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(default='', blank=True) 
    hobbies=models.CharField(max_length=255, default='', blank=True)
    cover = models.ImageField(upload_to='images/',default='default.jpg')


    def __str__(self):
        return '%s' % self.title