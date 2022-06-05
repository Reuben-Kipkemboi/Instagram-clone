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

