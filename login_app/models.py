from django.db import models
from django.contrib.auth.models import UserManager
import re	# the regex module

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}
        
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        
        if len(post_data['fname']) < 2:
            errors['fname'] = "First Name must be at least 2 characters"

        if len(post_data['lname']) < 2:
            errors['lname'] = "Last Name must be at least 2 characters"

        if len(post_data['password']) < 8:
            errors['pasword'] = "Password has to be a minimum of 8 characters"

        return errors



class User(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=40)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager() # add this line!
