from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=20)
    Roll_no=models.CharField(max_length=20)
    Father_name=models.CharField(max_length=20)
    Department=models.CharField(max_length=20)
    Address=models.TextField()
    
    
    def __str__(self):
        return self.Name
