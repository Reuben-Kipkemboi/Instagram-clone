from django.contrib import admin
from .models import Profile, Instagram_post, User_comment, User_likes

# Register your models here.
admin.site.register(Profile),
admin.site.register(Instagram_post),
admin.site.register(User_likes),
admin.site.register(User_comment)
