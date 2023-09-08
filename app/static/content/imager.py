from PIL import Image,ImageFont,ImageDraw
import textwrap
import os
import random


def render_tweets(tweets,fontsrc, imagepath, homepath):
	a= tweets
	picname=imagepath
	
	basewidth = 1200
	img = Image.open(picname)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	os.chdir(homepath)
	try:
		img.save(picname)
	except:
		img=img.convert('RGB')
		img.save(picname)

	img=Image.open(picname)  #load pic
	os.remove(picname)		#delete after load

	#Add Glitch Effect
	from glitch_this import ImageGlitcher
	glitcher = ImageGlitcher()
	img = glitcher.glitch_image(img, 2, color_offset=True, scan_lines=False)
	# Done glitching to loaded image

	os.chdir(homepath)
	font = ImageFont.truetype(fontsrc, 50,layout_engine=ImageFont.LAYOUT_RAQM)
	draw=ImageDraw.Draw(img)
	text=a

	#some deadly calculation to kepp text at center
	para = textwrap.wrap(text, width=45)
	MAX_W, MAX_H = 1200, 627
	current_h, pad = 200, 10
	for line in para:
		w, h = draw.textsize(line, font=font)
		
		x1,y1=((MAX_W - w)/2),current_h
		drw =ImageDraw.Draw(img,'RGBA')
		##
		drw.polygon([(x1,y1),(x1+w,y1),(x1+w,y1+h),(x1,y1+h)],(0,0,0,200))
		del drw
		
		draw.text(((MAX_W - w) / 2, current_h-8), line, (255,20,147), font=font)
		draw.text(((MAX_W - w) / 2+4, current_h-4), line, (65,105,225), font=font)
		draw.text(((MAX_W - w) / 2+8, current_h), line, (250, 255, 250
		), font=font)
		current_h += h + pad
		#255, 105, 180 dark pink, 255, 182, 193
		#purple dark 128,0,128
		#deep pink 255,20,147,  -65,105,225


	#it was my code
	'''
	font=ImageFont.truetype("ub.ttf",25)
	draw.text((10,570),b,(255,255,255),font=font)
	'''
	k=str(random.randint(1,2000))
	name="newpic"+k+".jpg"
	try:
		img.save(name)
	except:
		img=img.convert('RGB')
		img.save(name)



def render_lines(lines,fontsrc, imagepath, homepath):
	a= lines
	picname=imagepath

	basewidth = 1200
	img = Image.open(picname)
	wpercent = (basewidth/float(img.size[0]))
	hsize = int((float(img.size[1])*float(wpercent)))
	img = img.resize((basewidth,hsize), Image.ANTIALIAS)
	os.chdir(homepath)
	try:
		img.save(picname)
	except:
		img=img.convert('RGB')
		img.save(picname)


	img=Image.open(picname)  #load pic
	os.remove(picname)		#delete after load

	#Add Glitch Effect
	from glitch_this import ImageGlitcher
	glitcher = ImageGlitcher()
	img = glitcher.glitch_image(img, 2, color_offset=True, scan_lines=False)
	# Done glitching to loaded image

	os.chdir(homepath)
	font = ImageFont.truetype(fontsrc, 50,layout_engine=ImageFont.LAYOUT_RAQM)
	draw=ImageDraw.Draw(img)
	poems=a
	#text itself is a list of lines of poems/songs
	text=[]
	for line in poems:
		line=line.replace("EmbedShare","")
		line=line.replace("URLCopyEmbedCopy","")
		line=line.replace("Embed","")
		sentences=textwrap.wrap(line, width=45)
		for sentence in sentences:
			text.append(sentence) 

	#some deadly calculation to kepp text at center
	para = text
	MAX_W, MAX_H = 1200, 627
	current_h, pad = 200, 10
	for line in para:
		w, h = draw.textsize(line, font=font)
		
		x1,y1=((MAX_W - w)/2),current_h
		drw =ImageDraw.Draw(img,'RGBA')
		##
		drw.polygon([(x1,y1),(x1+w,y1),(x1+w,y1+h),(x1,y1+h)],(0,0,0,200))
		del drw
		
		draw.text(((MAX_W - w) / 2, current_h-8), line, (255,20,147), font=font)
		draw.text(((MAX_W - w) / 2+4, current_h-4), line, (65,105,225), font=font)
		draw.text(((MAX_W - w) / 2+8, current_h), line, (250, 255, 250
		), font=font)
		current_h += h + pad
		#255, 105, 180 dark pink, 255, 182, 193
		#purple dark 128,0,128
		#deep pink 255,20,147,  -65,105,225


	#it was my code
	'''
	font=ImageFont.truetype("ub.ttf",25)
	draw.text((10,570),b,(255,255,255),font=font)
	'''
	#k=str(random.randint(1,100))

	k=str(random.randint(1,2000))
	name="newpic"+k+".jpg"
	try:
		img.save(name)
	except:
		img=img.convert('RGB')
		img.save(name)