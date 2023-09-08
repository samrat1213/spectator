

from static.content.randomlines import getrandomlines
from static.content.find import main, return_lines, getline
import random
from static.content.clean import clean
from static.content.imager import render_lines, render_tweets
from static.content.imagelink import newlink
import os
import time
import urllib.request

#homepath="/home/phantom/Desktop/tempo/heroku/"
homepath="/app/static/content/"
#homepath is a picture to be saved
fontsrc=homepath+"fonts/"
songspath=homepath+"lyrics/"
tweetspath=homepath+"tweets/"
poemspath=homepath+"poems/topics/"
destination=homepath+"creations"

def  generate_random(content_type, language, imagepath, fontpath):

	if content_type == "t": 
		string=getrandomlines(tweetspath)
		print(string)
		string, dirname, filename =getline(string, tweetspath, language)
		string=clean(string)
		if language=="nep": print(string)
		render_tweets(string, fontpath, imagepath, destination)
	elif content_type=="s":
		string=getrandomlines(songspath)
		string=main(string, songspath, homepath, language)
		render_lines(string, fontpath, imagepath, destination)
	else:
		string=getrandomlines(poemspath)
		string=main(string, poemspath, homepath, language)
		render_lines(string, fontpath, imagepath, destination)

def generate(search_term, content_type, picture_type, language):
	link=newlink(homepath, picture_type)
	urllib.request.urlretrieve(link,homepath+"creations/temp.jpg")
	imagepath=homepath+"creations/temp.jpg"
	fontpath=fontsrc+random.choice(os.listdir(homepath+"fonts"))

	#print("P:poems T: tweets S: songs")
	#print("Press Enter For Random")
	content=content_type

	#print("N: Nepali ENTER: English")
	language=language

	if language=="": language="en"
	else: 
		language="nep"
		fontpath=homepath+"nepali.ttf"

	if search_term == "ranDom":
		generate_random(content_type, language, imagepath, fontpath)


	elif content=="t": 
			string, dirname, filename =getline(search_term, tweetspath, language)
			string=clean(string)
			print(string)
			render_tweets(string, fontpath, imagepath, destination)

	elif  content=="p": 
		string=main(search_term, poemspath, homepath, language)
		render_lines(string, fontpath, imagepath, destination)

	elif content=="s": 
		string=main(search_term, songspath, homepath, language)
		render_lines(string, fontpath, imagepath, destination)

	else: pass


def  generate_random_text(content_type, language):

	if content_type == "t": 
		string=getrandomlines(tweetspath)
		print(string)
		string, dirname, filename =getline(string, tweetspath, language)
		string=clean(string)
		if language=="nep": print(string)
		return string
	elif content_type=="s":
		string=getrandomlines(songspath)
		string=main(string, songspath, homepath, language)
		return string
	else:
		string=getrandomlines(poemspath)
		string=main(string, poemspath, homepath, language)
		return string

def generate_text(search_term, content_type, language):

	#print("P:poems T: tweets S: songs")
	#print("Press Enter For Random")
	content=content_type

	#print("N: Nepali ENTER: English")
	language=language

	if language=="": language="en"
	else: 
		language="nep"

	if search_term == "ranDom":
		string= generate_random_text(content_type, language)
		return string


	elif content=="t": 
			string, dirname, filename =getline(search_term, tweetspath, language)
			string=clean(string)
			print(string)
			return string

	elif  content=="p": 
		string=main(search_term, poemspath, homepath, language)
		return string

	elif content=="s": 
		string=main(search_term, songspath, homepath, language)
		return string

	else: pass


def  create(search_term, content_type, picture_type, language):
	list1=os.listdir(destination)
	for item in list1:
		os.remove(destination+"/"+item)
	for i in range(0,10):
		generate(search_term, content_type, picture_type, language)
	list1=os.listdir(destination)
	return list1


def get_text(search_term, content_type, language):
	lists=[]
	for i in range(0,10):
		string=generate_text(search_term, content_type, language)
		lists.append(string)
	return lists
