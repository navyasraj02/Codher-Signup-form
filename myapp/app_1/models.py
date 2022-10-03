from codecs import getencoder
from platform import python_version
from django.db import models


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
    password = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.emailAdd
