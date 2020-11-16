from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/avatar/%Y/%m/%d/',null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.avatar)

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

class Article(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE,null=True,blank=True)
    name = models.TextField(null=True,blank=True)
    genre = models.ForeignKey('articles.Genre', on_delete=models.CASCADE)
    headline = models.TextField(null=True,blank=True)
    content = models.TextField(null=True,blank=True)
    image = models.ImageField(upload_to='media/images/%Y/%m/%d/',null=True,blank=True)
    videofile= models.FileField(upload_to='media/videos/%Y/%m/%d/', null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '{}'.format(self.headline)

class Comment(models.Model):
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments',blank=True,null=True)
    name = models.CharField(max_length=80,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    body = models.TextField(blank=True,null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    active = models.BooleanField(default=False,blank=True,null=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
class Suggestions(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(_('email address'))
    company = models.CharField(max_length=225,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True)
    message = models.CharField(max_length=1000,null=True,blank=True)
