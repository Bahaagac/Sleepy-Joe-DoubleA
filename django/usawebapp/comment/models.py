from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Comment(models.Model):
    nickName = models.CharField(max_length = 30,verbose_name = "Name")
    userComment = models.CharField(max_length = 300,verbose_name = "Comment")

    def __str__(self):
        return "Name: " +self.nickName + " || " + "Comment: " + self.userComment


class Review(models.Model):
    expertName = models.CharField(max_length = 30,verbose_name = "expertName")
    expertCompany = models.CharField(max_length = 30,verbose_name = "expertCompany")
    review = models.CharField(max_length = 300,verbose_name = "expertReview")

    def __str__(self):
        return "expertName: " +self.expertName + " || " + "expertCompany: " + self.expertCompany + " || " + "expertReview" + self.review