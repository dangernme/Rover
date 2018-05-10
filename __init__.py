from flask import Flask, render_template ,request
import sys
import os
import logging
from logging.handlers import RotatingFileHandler
from importlib.machinery import SourceFileLoader

tmp = SourceFileLoader("module.name", "/var/www/RoverApp/RoverApp/python/buzzer.py").load_module()
buz = tmp.Buzzer()

app = Flask(__name__)  

@app.route('/') 
@app.route('/controls')
def controls():   
    app.logger.warning("bla bla")
    return render_template("controls.html")#, dir=buz)

@app.route('/configuration') 
def configuration():     
	return render_template("configuration.html")
	
@app.route('/debug') 
def debug():     
	return render_template("debug.html")

if __name__ == "__main__":
    handler = RotatingFileHandler('rover.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.run()	