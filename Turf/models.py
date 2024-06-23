from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserType(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)

class Userreg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

class Ownerreg(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    owner_addr = models.CharField(max_length=50)

class Turf(models.Model):
    owner = models.ForeignKey(Ownerreg, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    descri = models.CharField(max_length=50)
    facility = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    image1 = models.ImageField(upload_to='images/')
    image2 = models.ImageField(upload_to='images/')
    image3 = models.ImageField(upload_to='images/',null=True)
    status = models.CharField(max_length=50)


class BookTurf(models.Model):
    user = models.ForeignKey(Userreg, on_delete=models.CASCADE)
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    b_date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    noh = models.CharField(max_length=50)
    forwhat = models.CharField(max_length=50,null=True)
    total = models.CharField(max_length=50)
    pack = models.CharField(max_length=50,null=True)
    status = models.CharField(max_length=50)

class Package(models.Model):
    turf = models.ForeignKey(Turf, on_delete=models.CASCADE)
    pack = models.CharField(max_length=50)
    fdate = models.CharField(max_length=50,null=True)
    tdate = models.CharField(max_length=50,null=True)
    discount = models.CharField(max_length=50,null=True)

class Feedback(models.Model):
    user = models.ForeignKey(Userreg, on_delete=models.CASCADE)
    feed = models.CharField(max_length=50)

