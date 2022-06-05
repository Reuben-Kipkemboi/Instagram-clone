import profile
from django.test import TestCase
from . models import *
from django.contrib.auth.models  import User 

# Create your tests here.
class TestLikes(TestCase):
    def setUp(self):
        self.new_like=User_likes(Instagram_post = self.Instagram_post)

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_like,User_likes))
        
 # Testing Save Method
    def test_save_method(self):
        self.new_like.save_like()
        likes = User_likes.objects.all()
        self.assertTrue(len(User_likes) > 0)
        
#TestingDelete methods
    def test_delete_likes(self):
        self.new_likes.save_user_likes()
        User_likes.objects.get(id =self.like.id).delete()
        likes = User_likes.objects.all()
        self.assertTrue(len(likes)==0)
        
#Profile

class TestProfile(TestCase):
    def setUp(self):
        self.new_user_profile=Profile(user = "test_user", profile_pic ='user.jpg')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_user_profile,  Profile))
        
 # Testing Save Method
    def test_save_method(self):
        self.new_user_profile.save_user_profile()
        Profile = Profile.objects.all()
        self.assertTrue(len(Profile) > 0)
        
#TestingDelete methods
    def test_delete_likes(self):
        self.new_user_profile.save_user_profile()
        Profile.objects.get(id =self.user.id).delete()
        profiles = profile.objects.all()
        self.assertTrue(len(profiles)==0)
        
#Instagram post
        
class TestInstagram_post(TestCase):
    def setUp(self):
        self.new_post=Instagram_post(title = "test_image", caption ='test_image_caption', image='test.jpg')

# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post,  Instagram_post))
        
 # Testing Save Method
    def test_save_method(self):
        self.new_post.save_post()
        posts = Instagram_post.objects.all()
        self.assertTrue(len(posts) > 0)
        
#TestingDelete methods
    def test_delete_post(self):
        self.new_post.save_post()
        Instagram_post.objects.get(id =self.post.id).delete()
        posts = profile.objects.all()
        self.assertTrue(len(posts)==0)
        
        
    def test_update_post(self):
        self.user.save()
        self.post.save_post()
        self.post.update_caption('testing_update')
        caption_update=self.post.caption
        self.assertEqual(caption_update,'testing_update')
        

        
        



