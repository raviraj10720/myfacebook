from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    loc = models.CharField(max_length=20,blank=True)
    bio = models.TextField(max_length=300,blank=True)
    img = models.ImageField(upload_to='pics',default='defaultdp.png')

    def __str__(self):
        return self. user.username+'profile'


class userpost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.TextField(max_length=300,blank=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username+'post'
