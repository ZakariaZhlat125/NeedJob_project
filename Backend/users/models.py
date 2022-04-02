import datetime


from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser
    )
from django.utils import timezone

DISCOUNT_CODE_TYPER_CHOICES = [
    ('percent','Percentage-based'),
    ('value','value-based'),
]


class MyUserManger(BaseUserManager):
    def create_user(self,email,date_of_birth,password=None):

        if not email:
            raise ValueError('Users must hava an email address')

        user =self.model(
            email.self.normalize_email(email),
            date_of_birth =date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,date_of_birth,password=None):
        user=self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth
        )
        user.is_admin=True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    ##username =models.U
    email=models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    date_of_birth=models.DateField()
    is_active =models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    #credits =models.PositiveIntegerField(default=100)
    linkedin_token=models.TextField(blank=True ,default='')
    expiry_date=models.DateTimeField(null=True, blank=True)
    objects=MyUserManger()

    USERNAME_FIELD = 'email'
    REQURTED_FIELDS=['data_of_birth']

    def __str__(self):
        return self.email
    def has_perm(self,prem ,obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perm(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True
    
    @property
    def is_staff(self):
        "Is the user a member of staff"
        return self.is_admin
    
    """@property
    def is_out_of_credits(self):
        "Is the user out of credits"
        return self.credits > 0
    @property
    def has_sufficient_credits(self,cost):
        return self.credits - cost >= 0"""
    @property
    def linkedin_signed_in(self):
        return bool(self.linkedin_token) and self.expiry_date > timezone.now()