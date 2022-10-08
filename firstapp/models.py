from distutils.command.upload import upload
import email
from pydoc import describe
from turtle import title
from xml.etree.ElementTree import Comment
from django.db import models
from setuptools import Command

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    age=models.IntegerField()


    def __str__(self):
        return self.name
    
class define(models.Model):
    title=models.CharField(max_length=100)
    descrption=models.CharField(max_length=100)

class Createblok(models.Model):
    
        title=models.CharField(max_length=100)
        email=models.CharField(max_length=100)
        photo=models.ImageField(upload_to="myimage")
        youblok=models.CharField(max_length=250)
    