from flask import Flask, render_template
import datetime
import requests


import os

import time
import spacy
import random



homedir="/opt/render/project/src/app/"


app = Flask(__name__,
            static_url_path='', 
            static_folder=homedir+'static',
            template_folder=homedir+'templates')






@app.route('/')
def sepectation():
    return render_template('newhome.html')

@app.route('/contactcontent')
def contact():
    return render_template('contactcontent.html')

@app.route('/homecontent')
def home():
    return render_template('homecontent.html')




@app.route('/textcontent')
def texts():  
    lists=[]
    tweetlist=[]


    for i in range(1,10):
        dirc=homedir+"lyrics\\twets\\"
        tweetfile=random.choice(os.listdir(dirc))
        with open(dirc + tweetfile, encoding='utf-8') as f1:
            tweet=random.choice(f1.readlines())
            tweetlist.append(tweet)
    return render_template('textcontents.html', tweetlist=tweetlist)



@app.route('/pic')
def pic():
    piclist=os.listdir(homedir+'static/tgm')
    items=len(piclist)-6
    import random
    n=random.randint(0,items)
    images=piclist[n:n+6]
    return render_template('pictures.html',images=images)


if __name__ == '__main__':
    app.run(debug=True)








