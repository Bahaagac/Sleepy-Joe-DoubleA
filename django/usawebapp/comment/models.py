from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Comment(models.Model):
    nickName = models.CharField(max_length = 30,verbose_name = "Name")
    userComment = models.CharField(max_length = 300,verbose_name = "Comment")

    def __str__(self):
        return "Name: " +self.nickName + " || " + "Comment: " + self.userComment