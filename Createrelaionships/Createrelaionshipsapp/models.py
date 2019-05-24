from django.db import models

# Create your models here.

class Auther(models.Model):
    aname=models.CharField(max_length=20)
    amail=models.EmailField(max_length=30)
    def __str__(self):
        return self.aname
class Publisher(models.Model):
    pname=models.CharField(max_length=20)
    copies=models.IntegerField()
    def __str__(self):
        return self.pname
class Student(models.Model):
    sname=models.CharField(max_length=20)
    mobile=models.BigIntegerField()
    def __str__(self):
        return self.sname
class Book(models.Model):
    author=models.OneToOneField(Auther)
    publisher=models.ForeignKey(Publisher)
    student=models.ManyToManyField(Student)
    bname=models.CharField(max_length=50)
    bcost=models.IntegerField()
    def __str__(self):
        return self.bname