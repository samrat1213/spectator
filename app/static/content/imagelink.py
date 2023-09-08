import os 
import random

def newlink(homepath, pictype):
	filepath=homepath+"imagelinks/"
	list1=['retros.txt', 'aesthetic_and_stuff.txt', 'far_away_from_universe.txt', 'pleasingaesthetics.txt']
	if pictype=="r": file=list1[0]
	elif pictype=="as": file=list1[1]
	elif pictype=="fu": file=list1[2]
	elif pictype=="pa": file=list1[3]
	else: file=random.choice(list1)
	file=filepath+file
	f= open(file,'r')
	links=f.readlines()
	link=random.choice(links)
	f.close()
	return link