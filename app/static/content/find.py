import os
import random
from static.content.randomlines import getrandomlines

#os.chdir('lyrics/')

def getline(string,filespath,lang):
        sentences=[]
        os.chdir(filespath)
        list1=os.listdir()
        for dr in list1:
            os.chdir(filespath+dr)
            list2=os.listdir()
            for file in list2:
                f1=open(file,'r')
                lines=f1.readlines()
                for line in lines:
                        if len(line)>1000:
                            break
                        string=string.lower()
                        line=line.lower()
                        test= string in line
                        if test == True:
                            line=line.strip()
                            sentences.append([line, str(file), str(dr)])
        print(len(sentences))
        sentence=random.choice(sentences)
        filename=sentence[1]
        dirname=sentence[2]
        sentence=sentence[0]
        sentence=sentence.replace("&amp;","and")
        if lang=="n":
            from googletrans import Translator
            translator = Translator()
            print(sentence)
            sentence = translator.translate(sentence,src='en', dest='ne')
            sentence=sentence.text
        else:
            pass

        return sentence, dirname, filename 


def return_lines(search_string, language, filespath):
	sentence, dirname, filename=getline(string=search_string, filespath=filespath , lang="en")
	file=open(filespath+dirname+"/"+filename,"r")
	text=file.readlines()

	a=-1
	while True:
		a=a+1
		line=text[a]
		sentence=sentence.lower()
		line=line.lower().strip()
		if sentence == line:
			break
	i=1
	count=0  #"no. of lines to print
	English=[]
	while True:
		try:
			line=text[a-3+i].strip()
			English.append(line)
			count=count+1
		except: pass
		i=i+1
		if count==4: break
		elif i>len(text): break
		else: pass
	

	Nepali=[]
	if language=="nep":
		from googletrans import Translator
		translator = Translator()
		
		for sentence in English:
			if sentence!="":
				sentence = translator.translate(sentence,src='en', dest='ne')
				sentence=sentence.text
				Nepali.append(sentence)
	return filename, dirname, English, Nepali




def main(search_string, filespath, homedir, language):
	filename, dirname, English, Nepali=return_lines(search_string=search_string, language=language, filespath=filespath)
	print( ".............................")
	print( "---English Text----")
	print()
	for line in English:
		if line!="": print(line)

	if language=="nep":
		print()
		print( "---Nepali Text----")
		print()
		for line in Nepali:
			if line!="": print(line)
			#print ("text: ",sentence)
	print()
	print( ".............................")
	print ("filename: ",filename)
	print ("directory: ",dirname)
	print( "...")
	print()


	os.chdir(homedir)
	try:
		file=open("num.txt","r")
		num=int(file.readlines()[0].strip())+1
		file.close()
	except:
		num=6
	file=open("num.txt","w")
	file.write(str(num)+"\n")
	file.close()

	file=open("history.txt","a")
	file.write(str(num)+"::------------------------\n")
	file.write("------------------------\n")
	file.write( "---Eng Text----\n")
	for line in English:
		file.write(line+"\n")
	file.write("\n")
	if language=="nep":
		file.write( "---Nep Text----\n")
		for line in Nepali:
			file.write(line+"\n")
	file.write(filename+"\n")
	file.write(dirname+"\n")
	file.write("\n")

	if language!="en": return Nepali
	else: return English

'''
while True:
	search_string=str(input("enter search term:"))
	if search_string=="":
		search_string=getrandomlines(filespath)
	if search_string=="xx": break
	lang=str(input("enter n for nepali:"))
	if lang!="n": language ="en"
	else: language ="nep"
	#try:
	main(search_string, language)
	#except: pass
'''

