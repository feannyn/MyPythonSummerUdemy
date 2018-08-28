from django.db import models

# Create your models here.
class User(models.Model):
	#instantiate and intialize the attributes of the tuples in the DB 
	f_name = models.CharField(max_length = 50) 
	l_name = models.CharField(max_length = 50)
	email =  models.EmailField(max_length = 50, unique = True)

	#create a string output function to output the define attribute of a tuple.
	def __str__(self):
		return self.email
