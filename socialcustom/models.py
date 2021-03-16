# from django.db import models
# from django.db.models import CharField
# # Create your models here.
# class User(models.Model):
#     Username = models.CharField(max_length=128 , unique=False)
#     email = models.EmailField(max_length=254)
#     password = models.CharField(max_length=10)
#     # password2 = models.CharField(max_length=12)


from __future__ import unicode_literals
from django.db import models
import django_tables2 as tables

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if (postData['first_name'].isalpha()) == False:
            if len(postData['first_name']) < 2:
                errors['first_name'] = "First name can not be shorter than 2 characters"

        if (postData['last_name'].isalpha()) == False:
            if len(postData['last_name']) < 2:
                errors['last_name'] = "Last name can not be shorter than 2 characters"

        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email"

        if len(postData['password']) < 8:
            errors['password'] = "Password is too short!"

        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()




class StatusMaster(models.Model):
    class Meta:
                app_label = "socialcustom"
                managed = True
    status = models.IntegerField(primary_key=True)
    StatusName = models.CharField(max_length=255)

class PropertyMaster(models.Model):
    accountId = models.BigIntegerField()
    acres = models.FloatField()
    adTargetingCountyId = models.BigIntegerField()
    address = models.CharField(max_length=255)
    baths = models.BigIntegerField()
    beds = models.BigIntegerField()
    brokerCompany= models.CharField(max_length=255)
    brokerName = models.CharField(max_length=255)
    Url = models.URLField(max_length=255)
    city = models.CharField(max_length=255)
    cityID= models.BigIntegerField()
    companyLogoDocumentId = models.BigIntegerField()
    county= models.CharField(max_length=255)
    countyId = models.BigIntegerField()
    description = models.TextField(max_length=255)
    hasHouse = models.BooleanField()
    hasVideo = models.BooleanField()
    hasVirtualTour = models.BooleanField()
    hasVirtualTour = models.BigIntegerField()
    imageCount = models.BigIntegerField()
    imageAltTextDisplay = models.CharField(max_length=255)
    # PK_id = models.BigIntegerField(default=0)
    isHeadlineAd = models.BooleanField()
    lwPropertyId = models.BigIntegerField()
    isALC = models.BigIntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    price = models.FloatField()
    types = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    status = models.BigIntegerField()
    zip = models.BigIntegerField()
    Rate = models.FloatField(default=0)
    Descrpt = models.TextField(max_length=255,default="!")
    created_at = models.DateTimeField(auto_now_add=True)

    # MY_CHOICES = (
    #     ('a', 'Hola'),
    #     ('b', 'Hello'),
    #     ('c', 'Bonjour'),
    #     ('d', 'Boas'),
    # )
    # my_field = models.CharField(max_length=1, choices=MY_CHOICES)

class TypeMaster(models.Model):
    class Meta:
                app_label = "socialcustom"
                managed = True
    TypeId = models.IntegerField()
    TypeName = models.CharField(max_length=255)

class Property_TypeMaster(models.Model):
        class Meta:
                app_label = "socialcustom"
                managed = True
                # unique_together = (('lwPropertyId', 'TypeId'),)
        Prop_Id2 = models.IntegerField(default=0)
        Type_Id2 = models.IntegerField(default=0)
        # Prop_Id = models.ManyToManyField(PropertyMaster)
        # Type_Id = models.ManyToManyField(TypeMaster)
        # TypeId = models.ForeignKey(TypeMaster, on_delete=models.CASCADE)
        # lwPropertyId = models.ForeignKey(PropertyMaster, on_delete=models.CASCADE)
        #









