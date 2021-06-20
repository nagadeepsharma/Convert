from django.db import models

#class Contact(models.Model):
    #first_name = models.CharField(max_length=30)
    #last_name = models.CharField(max_length=30)

class filesUpload(models.Model):
    file = models.FileField()    

class ImageUpload(models.Model):
    File = models.ImageField(upload_to="images/")  