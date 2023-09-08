import os 
import random


def getrandomlines(filepath):

	#print(os.getcwd())
	
	os.chdir(filepath)

	list1=os.listdir()
	folder=random.choice(list1)
	os.chdir(folder)


	#list2=os.listdir()
	#folder=random.choice(list2)
	#os.chdir(folder)
	#print(os.getcwd())

	list3=os.listdir()
	file=random.choice(list3)
	f1=open(file)

	list3=f1.readlines()
	randomline=random.choice(list3)


	return randomline.strip()

