#imports
from email.mime import image
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


#APPLICATION MODELS
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=False)
    image = CloudinaryField('profile_pic')
    date_joined= models.DateField(auto_now_add=True)
    
    # def __str__(self):
    #     return self.user
    

class Instagram_post(models.Model):
    title =models.CharField(max_length=200, null=False)
    caption= models.TextField(max_length=500, null=True)
    creator= models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted= models.DateField(auto_now_add=True)
    profile_of_creator= models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = CloudinaryField('image', blank=True)
    
    def __str__(self):
        return self.title
    


    
class User_likes(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Instagram_post, on_delete=models.CASCADE)
    
    
class User_comment(models.Model):
    content = models.TextField( null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Instagram_post, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    



