from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    mobileno = models.CharField(max_length=255, default='', blank=True)
    email = models.CharField(max_length=255, default='', blank=True)
    place = models.CharField(max_length=255, default='', blank=True)
    course = models.CharField(max_length=255, default='', blank=True)
    organization = models.CharField(max_length=255, default='', blank=True)
    softwareskills=models.CharField(max_length=255, default='', blank=True)
    programmingskills=models.CharField(max_length=255, default='', blank=True)
    hobbies=models.CharField(max_length=255, default='', blank=True)
    fname=models.CharField(max_length=255, default='', blank=True)
    mname=models.CharField(max_length=255, default='', blank=True)
    dob=models.CharField(max_length=255, default='', blank=True)
    gender=models.CharField(max_length=255, default='', blank=True)
    language=models.CharField(max_length=255, default='', blank=True)
    marital=models.CharField(max_length=255, default='', blank=True)
    address=models.CharField(max_length=255, default='', blank=True)


    def __str__(self):
        return '%s' % self.title