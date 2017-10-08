from django.db import models

# Create your models here.

class Entry (models.Model):
	name1 = models.CharField (max_length = 100, unique = True)
	name2 = models.CharField (max_length = 100, unique = True)
	count = models.IntegerField ()
