from codecs import getencoder
from concurrent.futures.process import _ResultItem
from platform import python_version
from django.db import models

# Create your models here.


class AddDetails(models.Model):
    emailAdd = models.EmailField(max_length=100)
    phoneNo = models.CharField(max_length=10, null=False, blank=False)
    genderOp = (('male', "MALE"),
                ('female', "FEMALE"),
                ('others', "OTHERS"))
    gender = models.CharField(max_length=10, choices=genderOp, default="male")
    bio = models.TextField()
    jobRole = models.CharField(max_length=200, null=False, blank=False)
    interests = models.CharField(max_length=200, null=False, blank=False)
    password = models.CharField(max_length=50)
