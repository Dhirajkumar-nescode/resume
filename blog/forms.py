from django.forms import ModelForm
from django.db import models
from .models import Blog



class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'mobileno','email','place','course','organization','softwareskills','programmingskills','hobbies','fname','mname','dob','gender','language','marital','address']