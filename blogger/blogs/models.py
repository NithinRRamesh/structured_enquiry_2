from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    title= models.CharField(max_length=60,)
    description = models.CharField(max_length=3000)
    pub_date = models.DateTimeField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    def __str__(self):
        return self.title