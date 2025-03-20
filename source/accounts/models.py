from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    
    def __str__(self):
        return (f"name of the user :  {self.username}")