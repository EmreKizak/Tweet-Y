from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tweet(models.Model):
    username = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    nickname = models.CharField(max_length=50)
    message = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',blank=True)
    publishing_date = models.DateTimeField(verbose_name='Paylaşma Tarihi',auto_now_add=True)
    
    def __str__(self):
        return f"Tweet user: {self.username} Tweet nick: {self.nickname} message: {self.message}"
    
    class Meta:
        ordering =['-publishing_date']
