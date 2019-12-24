from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.contrib import auth

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='profile_image', blank=True)
	first = models.CharField(max_length=30, blank = True)
	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])
        
post_save.connect(create_profile, sender=User)

# def timepass(self, **kwargs):
#     user_profile = UserProfile.objects.create(
#         user=self,
#         **kwargs # you can pass other fields values upon creating
#     )
# auth.models.User.add_to_class('timepass', timepass)
