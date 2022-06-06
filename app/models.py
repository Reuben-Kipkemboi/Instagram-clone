#imports
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
#post_save is the signal that is sent at the end of the save method.
from django.db.models.signals import post_save
from django.dispatch import receiver



#APPLICATION MODELS
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=False)
    image = CloudinaryField('profile_pic')
    date_joined= models.DateField(auto_now_add=True)
    
    def save_user_profile(self):
        self.save()
        
#     @receiver(post_save, sender=User)
#     def create_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
        
# # # A profile is creted everytime a user is created
# # #User is the sender which is responsible for making the notification.

#     @receiver(post_save, sender=User)
#     def save_profile(sender, instance, **kwargs):
#         instance.profile.save()
    
    def delete_profile(self):
        self.save() 
        
       
    def __str__(self):
        return self.user.username
    
    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term).all()
        return profiles
    
#Class Instagram posts ---simply posts 
class Instagram_post(models.Model):
    title =models.CharField(max_length=200, null=False)
    caption= models.TextField(max_length=500, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted= models.DateField(auto_now_add=True)
    # profile_of_creator= models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    image = CloudinaryField('image', blank=True)
    
    def __str__(self):
        return self.title
    
    def save_post(self):
        self.save()
        
    def delete_post(self):
        self.delete()
        
    @classmethod
    def search_post(cls, search_term):
        posts = cls.objects.filter(title__icontains=search_term).all()
        return posts
        
class User_likes(models.Model):
    person_liking = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Instagram_post,related_name='likes_count', on_delete=models.CASCADE)
    
    
    def save_user_likes(self):
        self.save()
        
    def delete_user_likes(self):
        self.delete()
        
        
    def number_of_user_likes(self):
        return self.likes.count()
    
    
class User_comment(models.Model):
    content = models.TextField( null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Instagram_post, on_delete=models.CASCADE)
    commented_at= models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.content
    
    def save_user_comments(self):
        self.save()
        
    def delete_user_comments(self):
        self.delete()
        
#a class to save our registered users to send mail     
class NewsLetterRecipients(models.Model):
    user = models.CharField(max_length = 30)
    email = models.EmailField()
    



