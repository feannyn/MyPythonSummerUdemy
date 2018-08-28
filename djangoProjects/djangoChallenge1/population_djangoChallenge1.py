#import the os library 
import os

#configure settings for the project
#set up the default environment 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'djangoChallenge1.settings')

#import django
import django 
django.setup()


import random 

from djangoChallenge1App.models import User
from faker import Faker

#initialize the faker populator
fakegen = Faker()

#create a function to add users to the database
def add_User(num = 5):
	#loop to create however many entries passed in
	for entry in range(num):
		fake_fn = fakegen.first_name()
		fake_ln = fakegen.last_name()
		fake_email = fakegen.email()
		u = User.objects.get_or_create(f_name = fake_fn, l_name = fake_ln, email = fake_email)[0]
		u.save()
	return u

if __name__ == '__main__':
		print("Populating the database...")
		add_User(20)
		print("Database has been populated")