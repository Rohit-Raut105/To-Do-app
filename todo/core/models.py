from django.db import models

# Create your models here.
class UserData(models.Model):
    first_name = models.CharField(max_length= 50, null=True, blank= False,verbose_name= "Enter your First Name.")
    last_name = models.CharField(max_length= 50, null= True, blank= False,verbose_name= "Enter your Last Name.")
    phone = models.CharField(max_length= 50, null= True , blank= False,verbose_name= "Enter your phone.")
    email = models.CharField(max_length= 50, null= True, blank= False,verbose_name= "Enter your email.")
    message = models.CharField(max_length= 50, null= True, blank= False,verbose_name= "Enter your message.")
    # Initilizating value of database
    def __str__(self) :
        return (self.first_name)