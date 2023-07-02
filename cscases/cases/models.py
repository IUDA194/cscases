from django.db import models

class User(models.Model):
    user_id = models.CharField(max_length=100)
    balance = models.IntegerField()

class Cases(models.Model):
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    item_id = models.CharField(max_length=200)

class inventory(models.Model):
    user_id = models.CharField(max_length=100)
    item = models.CharField(max_length=200)
    date = models.DateField()

class contract(models.Model):
    item_id = models.CharField(max_length=100)
    can_drop = models.CharField(max_length=200)
    chanse = models.IntegerField()