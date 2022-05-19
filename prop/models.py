from django.db import models


# Create your models here.


class Contect_us(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=10)
    msg = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class Contect_okk(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=10)
    msg = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
