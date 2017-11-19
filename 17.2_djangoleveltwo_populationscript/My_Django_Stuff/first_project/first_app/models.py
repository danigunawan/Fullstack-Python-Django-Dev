# models.py ini berfungsi untuk store data aplikasi berhubungan dengan model database
# contoh :
# Membuat kelas model Dog.
# class Dog(models.Model):
# name = models.CharField(max_length = 45)
# breed = models.CharField(max_length = 45)
# created_at = models.DateTimeField(auto_now_add = True)
# updated_at = models.DateTimeField(auto_now_add = True)

from django.db import models

# Create your models here.


class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name


class Webpage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
