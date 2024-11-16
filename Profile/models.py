from django.db import models


# Create your models here.
class UserModel(models.model):

    user_name = models.CharField(max_length=20,verbose_name="user_name")
    email = models.EmailField(max_length=254,verbose_name="email")
    phone_number = models.CharField(max_length=50 , verbose_name=" phone_number")


    def __str__(self):
        return self.user_name
    

    
