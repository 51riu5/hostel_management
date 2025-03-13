from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class studentgeninfo(models.Model):
    name = models.CharField(max_length=50)
    rollno = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    contactno = models.CharField(max_length=11)
    yearofstudy = models.CharField(max_length=50)
    dob = models.DateField()
    bloodgroup=models.CharField(max_length=20)
    nationality=models.CharField(max_length=50)
    mothertongue=models.CharField(max_length=50)
    aadhaar=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    

    def __str__(self):
        return self.name
