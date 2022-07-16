from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#base manager class to handle the user class

class UserManager(BaseUserManager):
    def create_user(self, firstname, middlename, lastname, email, contact, password=None):
        if not firstname:
            raise ValueError("User first name is required")
        if not lastname:
            raise ValueError("User last name is required")
        if not email:
            raise ValueError("Email is required")
        if not contact:
            raise ValueError("Contact is required")

        user = self.model(
            firstname = firstname,
            middlename = middlename,
            lastname = lastname, 
            email = self.normalize_email(email),
            contact = contact
        )

        # def create_superuser(self)

#class to handle signup fields for users

class User(AbstractBaseUser):
    firstname = models.CharField(verbose_name="firstname", max_length=100)
    middlename = models.CharField(verbose_name="middlename", max_length=100)
    lastname = models.CharField(verbose_name="lastname", max_length=100)
    email = models.EmailField(verbose_name="email", unique=True, max_length=100)
    contact = models.CharField(verbose_name="contact", unique=True, max_length=20)
    date_joined = models.DateTimeField(verbose_name="date_joined", auto_now=True)
    last_login = models.DateTimeField(verbose_name="last_login")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['firstname', 'middlename', 'lastname', 'contact']

    def __str__(self):
        return f"{self.firstname} + {self.lastname}"

    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perm(self, app_label):
        return True