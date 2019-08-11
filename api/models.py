from django.db import models

# Create your models here.
#class Companies(models.Model):

class Companies(models.Model):
	name = models.CharField(max_length=100)
	address = models.CharField(max_length=200)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	value = models.IntegerField()
	name = models.CharField(max_length=255, blank=False, unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)
